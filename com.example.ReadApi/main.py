import sys
import time
import traceback
import requests

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from awsiot.greengrasscoreipc.model import (
    PublishMessage,
    BinaryMessage,
    SubscriptionResponseMessage,
    UnauthorizedError,
    QOS
)

import blickfeld_scanner
import json


def on_stream_event(event: SubscriptionResponseMessage) -> None:
    try:
        message = str(event.binary_message.message, 'utf-8')
        topic = event.binary_message.context.topic
        print('Received new message on topic %s: %s' % (topic, message))
    except:
        traceback.print_exc()


def on_stream_error(error: Exception) -> bool:
    print('Received a stream error.', file=sys.stderr)
    traceback.print_exc()
    return False  # Return True to close stream, False to keep stream open.


def on_stream_closed() -> None:
    print('Subscribe to topic stream closed.')


def fetch_bitcoin_info():
    apiUri = "https://api.coindesk.com/v1/bpi/currentprice.json"
    res = requests.get(apiUri)
    return res.json()


def connect_scanner():
    device_ip_or_hostname = "192.168.26.26"
    return blickfeld_scanner.scanner(device_ip_or_hostname)


def fetch_point_cloud(ipc_client):
    """Fetch the point cloud of a device and print the frame ID and number of returns in the received frame.

    This example will stop after 5 received frames.

    :param target: hostname or IP address of the device
    """
    device = connect_scanner()

    stream = device.get_point_cloud_stream()  # Create a point cloud stream object

    for i in range(5):
        # Receive a frame. This frame will also be dumped into the file
        frame = stream.recv_frame()
        # Format of frame is described in protocol/blickfeld/data/frame.proto or doc/protocol.md
        # Protobuf API is described in https://developers.google.com/protocol-buffers/docs/pythontutorial
        data = frame.scanlines[0].points[0].returns[0]
        thisdict = {
            "cartesianx": data.cartesian[0],
            "cartesiany": data.cartesian[1],
            "cartesianz": data.cartesian[2]
        }
        ipc_client.publish_to_iot_core(
            topic_name="iot/lidar", payload=bytes(json.dumps(thisdict), "utf-8"), qos=QOS.AT_LEAST_ONCE)
        print(f"Got {frame}")
    stream.stop()


def main():
    print('Starting reading API')
    time.sleep(10)
    try:
        ipc_client = GreengrassCoreIPCClientV2()
        # Subscription operations return a tuple with the response and the operation.
        _, operation = ipc_client.subscribe_to_topic(topic="test/testing", on_stream_event=on_stream_event,
                                                     on_stream_error=on_stream_error, on_stream_closed=on_stream_closed)
        print('Successfully subscribed to topic: ' + "test/testing")

        # Keep the main thread alive, or the process will exit.
        try:
            while True:
                binary_message = BinaryMessage(
                    message=bytes("hello there", 'utf-8'))
                publish_message = PublishMessage(binary_message=binary_message)
                ipc_client.publish_to_topic(
                    topic="test/testing", publish_message=publish_message)

                bitcoinInfo = fetch_bitcoin_info()
                ipc_client.publish_to_iot_core(topic_name="iot/testing", payload=bytes(
                    "Time: " + bitcoinInfo["time"]["updated"] + "\nBitcoin price: " + bitcoinInfo["bpi"]["EUR"]["rate"], "utf-8"), qos=QOS.AT_LEAST_ONCE)

                fetch_point_cloud(ipc_client=ipc_client)
                time.sleep(10)
        except InterruptedError:
            print('Subscribe interrupted.')

        # To stop subscribing, close the stream.
        operation.close()
    except UnauthorizedError:
        print('Unauthorized error while subscribing to topic: ' +
              "test/testing", file=sys.stderr)
        traceback.print_exc()
        exit(1)
    except Exception:
        print('Exception occurred', file=sys.stderr)
        traceback.print_exc()
        exit(1)


if __name__ == '__main__':
    main()

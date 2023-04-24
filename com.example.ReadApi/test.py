import blickfeld_scanner
import json


def connect_scanner():
    device_ip_or_hostname = "192.168.26.26"
    return blickfeld_scanner.scanner(device_ip_or_hostname)


def fetch_point_cloud():
    """Fetch the point cloud of a device and print the frame ID and number of returns in the received frame.

    This example will stop after 10 received frames.

    :param target: hostname or IP address of the device
    """
    device = connect_scanner()

    stream = device.get_point_cloud_stream()  # Create a point cloud stream object

    for i in range(10):
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
        print(f"Got {json.dumps(thisdict)}")
    stream.stop()


def main():
    print("Hello world")
    fetch_point_cloud()


if __name__ == '__main__':
    main()

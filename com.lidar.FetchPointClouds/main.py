import sys
import time
import traceback
from entities.lidar.frame import Frame

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from awsiot.greengrasscoreipc.model import (
    UnauthorizedError,
    QOS
)

import blickfeld_scanner
import jsonpickle

class LidarPublisher:
    def __init__(self, ipc_client: GreengrassCoreIPCClientV2, lidars) -> None:
        self.ipc_client = ipc_client
        self.lidars = lidars

    def publish_lidars_info(self):
        lidarsJson = jsonpickle.encode(self.lidars)
        self.ipc_client.publish_to_iot_core(
            topic_name="iot/lidar", payload=bytes("Hello from program", "utf-8"), qos=QOS.AT_LEAST_ONCE)
        self.ipc_client.publish_to_iot_core(
            topic_name="iot/lidar", payload=bytes(lidarsJson, "utf-8"), qos=QOS.AT_LEAST_ONCE)

class Lidar:
    def __init__(self, ip) -> None:
        self.ip = ip
        self.frame = None

    def connect_scanner(self):
        return blickfeld_scanner.scanner(self.ip)

    def fetch_point_cloud(self):
        device = self.connect_scanner()

        stream = device.get_point_cloud_stream()
        frame = stream.recv_frame()
        self.frame = Frame(frame)

        stream.stop()

def main():
    print('Starting fetching lidar data')
    try:
        ipc_client = GreengrassCoreIPCClientV2()
        lidar1 = Lidar("192.168.26.26")
        lidars = [lidar1]
        lidarPublisher = LidarPublisher(ipc_client, lidars)
        while True:
            lidar1.fetch_point_cloud()
            lidarPublisher.publish_lidars_info()
            time.sleep(10)

    except UnauthorizedError:
        print('Unauthorized error while posting/sub to topics', file=sys.stderr)
        traceback.print_exc()
        exit(1)
    except Exception as e:
        print("An error occurred:", e)
        print(traceback.format_exc())
        exit(1)

if __name__ == '__main__':
    main()
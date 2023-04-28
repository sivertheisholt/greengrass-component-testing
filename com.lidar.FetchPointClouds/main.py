import sys
import time
import traceback
from entities.lidar.point_cloud import PointCloud

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from awsiot.greengrasscoreipc.model import (
    UnauthorizedError,
    QOS
)

import blickfeld_scanner

class Lidar:
    def __init__(self, ip, ipc_client) -> None:
        self.ip = ip
        self.ipc_client = ipc_client

    def connect_scanner(self):
        return blickfeld_scanner.scanner(self.ip)

    def fetch_point_cloud(self):
        device = self.connect_scanner()

        stream = device.get_point_cloud_stream()

        for i in range(1):
            frame = stream.recv_frame()
            data = PointCloud(frame)
            print(f"Got {data.header.firmware_version}")
        stream.stop()

def main():
    try:
        ipc_client = GreengrassCoreIPCClientV2()
        lidar = Lidar("192.168.26.26", ipc_client)
        while True:
            lidar.fetch_point_cloud()
            time.sleep(60)

    except Exception:
        print('Exception occurred', file=sys.stderr)
        traceback.print_exc()
        exit(1)

if __name__ == '__main__':
    main()

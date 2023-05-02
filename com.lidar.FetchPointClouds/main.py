import time
import traceback

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2

from entities.lidar import Lidar
from entities.lidar_publisher import LidarPublisher

def main():
    print('Starting fetching lidar data')
    try:
        ipc_client = GreengrassCoreIPCClientV2()
        lidar1 = Lidar("192.168.26.26")
        lidars = [lidar1]
        lidarPublisher = LidarPublisher(ipc_client, lidars)
        while True:
            lidar1.fetch_point_cloud()
            lidarPublisher.upload_lidars_info()
            lidarPublisher.publish_lidars_info()
            time.sleep(10)
    except Exception as e:
        print("An error occurred:", e)
        print(traceback.format_exc())
        exit(1)

if __name__ == '__main__':
    main()
import time
import traceback

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from entities.lidar_cube_status.scanner import Scanner
import jsonpickle

from entities.lidar import Lidar
from entities.lidar_publisher import LidarPublisher

def main():
    print('Starting fetching lidar data')
    try:
        ipc_client = GreengrassCoreIPCClientV2()
        lidar1 = Lidar("192.168.26.26")
        lidars = [lidar1]
        lidarPublisher = LidarPublisher(ipc_client, lidars)
        failCount = 0
        while True:
            lidars[0].fetch_state()
            lidarPublisher.publish_lidars_status()
            if lidars[0].scanner_status.state != 2:
                failCount = 0
                lidar1.fetch_point_cloud()
                lidarPublisher.upload_lidars_frame()
                lidarPublisher.publish_lidars_frame()
            else:
                failCount = failCount + 1
            if failCount == 5:
                print("Something is wrong with the lidars, exiting after 5 tries")
                exit(1)
            time.sleep(10)
    except Exception as e:
        print("An error occurred:", e)
        print(traceback.format_exc())
        exit(1)

if __name__ == '__main__':
    main()
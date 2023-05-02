
import traceback
import sys
import boto3
import jsonpickle

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from awsiot.greengrasscoreipc.model import (
    UnauthorizedError,
    QOS
)

from entities.lidar_cube.frame import Frame

class LidarPublisher:
    def __init__(self, ipc_client: GreengrassCoreIPCClientV2, lidars):
        self.ipc_client = ipc_client
        self.lidars = lidars

    def publish_lidars_info(self):
        try:
            print("Publishing status to IoT core...")
            self.ipc_client.publish_to_iot_core(topic_name="iot/lidar", payload=bytes("Success", "utf-8"), qos=QOS.AT_LEAST_ONCE)
        except UnauthorizedError:
            print('Unauthorized error while publishing status to IoT core...', file=sys.stderr)
            traceback.print_exc()

    def upload_lidars_info(self):
        print("Uploading lidars info to s3 bucket...")
        s3 = boto3.resource('s3')

        lidarsJsonBytes = bytes(jsonpickle.encode(Frame(self.lidars[0].frame_data)), "utf-8")
        
        s3.Bucket("sivertheisholt").put_object(Key="lidar1.json", Body=lidarsJsonBytes)
        
        print('JSON file uploaded to S3.')
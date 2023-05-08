
import traceback
import boto3
import jsonpickle
import logging

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2
from awsiot.greengrasscoreipc.model import (
    UnauthorizedError,
    QOS
)

from entities.lidar_cube_frame.frame import Frame
from entities.lidar_cube_status.scanner import Scanner

class LidarPublisher:
    def __init__(self, ipc_client: GreengrassCoreIPCClientV2, lidars):
        self.ipc_client = ipc_client
        self.lidars = lidars

    def publish_lidars_frame(self):
        try:
            logging.info("Publishing status to IoT core")
            self.ipc_client.publish_to_iot_core(topic_name="iot/lidar/data", payload=bytes("Success", "utf-8"), qos=QOS.AT_LEAST_ONCE)
            logging.info("Successfully published status to IoT core")
        except UnauthorizedError:
            logging.info("'Unauthorized error while publishing status to IoT core")
            traceback.print_exc()
            exit(1)

    def upload_lidars_frame(self):
        logging.info("Uploading lidars info to s3 bucket")
        s3 = boto3.resource('s3')

        lidarsJsonBytes = bytes(jsonpickle.encode(Frame(self.lidars[0].frame_data)), "utf-8")
        
        s3.Bucket("sivertheisholt").put_object(Key="lidar1.json", Body=lidarsJsonBytes)
        
        logging.info('JSON file uploaded to S3')

    def publish_lidars_status(self):
        logging.info("Publishing lidars status to IoT core")
        class LidarStatus:
            def __init__(self, lidar):
                self.scanner = lidar.scanner_status
                self.temperature = lidar.temperatures
                self.time = lidar.time_synchronization
        
        data = bytes(jsonpickle.encode(LidarStatus(self.lidars[0])), "utf-8")
        self.ipc_client.publish_to_iot_core(topic_name="iot/lidars/status", payload=data, qos=QOS.AT_LEAST_ONCE)
        
        logging.info("Successfully published lidars status to Iot core")

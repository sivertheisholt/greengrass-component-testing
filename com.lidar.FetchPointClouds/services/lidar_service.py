from typing import List
from entities.lidar import Lidar
from entities.lidar_publisher import LidarPublisher

from awsiot.greengrasscoreipc.clientv2 import GreengrassCoreIPCClientV2

class LidarService:
    def __init__(self, lidars: List[Lidar], ipc_client: GreengrassCoreIPCClientV2 | None, py_env) -> None:
        self.lidars = lidars
        self.lidar_publisher = LidarPublisher(ipc_client, lidars)
        self.py_env = py_env

    def fetch_point_clouds(self):
        for lidar in self.lidars:
            lidar.fetch_point_cloud()
            
    def fetch_states(self):
        for lidar in self.lidars:
            lidar.fetch_state()

    def is_ready(self) -> bool:
        for lidar in self.lidars:
            if not lidar.is_ready():
                return False
        return True
            
    def run_data_handling(self):
        self.fetch_states()
        if self.py_env == "prod":
            self.lidar_publisher.publish_lidars_status()

        # If lidar status is ready then fetch/publish data
        if self.is_ready():
            self.fetch_point_clouds()
            if self.py_env == "prod":
                self.lidar_publisher.upload_lidars_frame()
                self.lidar_publisher.publish_lidars_frame()
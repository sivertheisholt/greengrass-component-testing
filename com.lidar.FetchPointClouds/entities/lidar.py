import blickfeld_scanner
import copy
import logging

from entities.lidar_cube_status.scanner import Scanner
from entities.lidar_cube_status.temperature import Temperature
from entities.lidar_cube_status.time_synchronization import TimeSynchronization
class Lidar:
    def __init__(self, ip):
        self.ip = ip
        self.frame_data = None
        self.scanner_status = None
        self.temperatures = None
        self.time_synchronization = None

    def is_ready(self) -> bool:
        return self.scanner_status.state == 2

    def connect_scanner(self):
        logging.info("Connecting to lidar")
        device = blickfeld_scanner.scanner(self.ip)
        logging.info("Device connected")
        return device

    def fetch_point_cloud(self):
        logging.info("Fetching point cloud")
        device = self.connect_scanner()

        logging.info("Getting stream")
        stream = device.get_point_cloud_stream()

        logging.info("Receiving frame")
        frame = stream.recv_frame()

        self.frame_data = copy.deepcopy(frame)

        stream.stop()
        
        logging.info("Done fetching point cloud")
        
    def fetch_state(self):
        logging.info("Fetching status")
        
        device = self.connect_scanner()
        status = device.get_status()

        status_data = copy.deepcopy(status)

        self.scanner_status = Scanner(status_data.scanner)
        self.temperatures = [Temperature(temp) for temp in status_data.temperatures]
        self.time_synchronization = TimeSynchronization(status_data.time_synchronization)

        logging.info("Done fetching status")
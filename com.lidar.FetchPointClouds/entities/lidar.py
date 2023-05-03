import blickfeld_scanner
import copy

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

    def connect_scanner(self):
        print("Connecting to lidar...")
        device = blickfeld_scanner.scanner(self.ip)
        print("Device connected")
        return device

    def fetch_point_cloud(self):
        print("Fetching point cloud...")
        device = self.connect_scanner()

        print("Getting stream...")
        stream = device.get_point_cloud_stream()

        print("Receiving frame...")
        frame = stream.recv_frame()

        self.frame_data = copy.deepcopy(frame)

        stream.stop()
        
        print("Done fetching point cloud")
        
    def fetch_state(self):
        print("Fetching status...")
        
        device = self.connect_scanner()
        status = device.get_status()

        status_data = copy.deepcopy(status)

        self.scanner_status = Scanner(status_data.scanner)
        self.temperatures = [Temperature(temp) for temp in status_data.temperatures]
        self.time_synchronization = status_data.time_synchronization

        print("Dont fetching status")
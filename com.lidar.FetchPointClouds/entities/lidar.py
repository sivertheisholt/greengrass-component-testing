import blickfeld_scanner
import copy

class Lidar:
    def __init__(self, ip):
        self.ip = ip
        self.frame_data = None

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
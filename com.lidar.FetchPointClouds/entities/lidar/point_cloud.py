from entities.lidar.header import Header
from entities.lidar.frame import Frame
from entities.lidar.scanline import Scanline

class PointCloud:
    def __init__(self, data: dict):
        self.header = Header(data.get("header"))
        self.frame = Frame(data.get("frame"))
        self.scanline = Scanline(data.get("scanline"))
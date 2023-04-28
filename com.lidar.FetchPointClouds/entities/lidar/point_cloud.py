from entities.lidar.header import Header
from entities.lidar.frame import Frame
from entities.lidar.scanline import Scanline

class PointCloud:
    def __init__(self, data: dict):
        self.header = Header(data.header)
        self.frame = Frame(data.frame)
        self.scanline = Scanline(data.scanline)
from entities.lidar_cube.header import Header
from entities.lidar_cube.frame import Frame
from entities.lidar_cube.scanline import Scanline

class PointCloud:
    def __init__(self, data: dict):
        self.header = Header(data.header)
        self.frame = Frame(data.frame)
        self.scanline = Scanline(data.scanline)
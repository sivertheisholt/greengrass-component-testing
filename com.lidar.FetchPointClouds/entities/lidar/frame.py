from entities.lidar.packed import Packed
from entities.lidar.algorithm import Algorithm
from entities.lidar.scan_pattern import ScanPattern
from entities.lidar.scanline import Scanline

import copy

class Frame:
    def __init__(self, data):
        self.data_copy = copy.deepcopy(data)
        self.id = self.data_copy.id
        self.start_time_ns = self.data_copy.start_time_ns
        self.scan_pattern = ScanPattern(self.data_copy.scan_pattern)
        self.is_ramp_up_phase = self.data_copy.is_ramp_up_phase
        self.total_number_of_points = self.data_copy.total_number_of_points
        self.total_number_of_returns = self.data_copy.total_number_of_returns
        self.scanlines = [Scanline(scanline) for scanline in self.data_copy.scanlines]
        self.packed = Packed(self.data_copy.packed)
        self.algorithms = [Algorithm(algorithm) for algorithm in self.data_copy.algorithms]
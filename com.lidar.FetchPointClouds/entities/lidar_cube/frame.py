from entities.lidar_cube.packed import Packed
from entities.lidar_cube.algorithm import Algorithm
from entities.lidar_cube.scan_pattern import ScanPattern
from entities.lidar_cube.scanline import Scanline
class Frame:
    def __init__(self, data):
        self.id = data.id
        self.start_time_ns = data.start_time_ns
        self.scan_pattern = ScanPattern(data.scan_pattern)
        self.is_ramp_up_phase = data.is_ramp_up_phase
        self.total_number_of_points = data.total_number_of_points
        self.total_number_of_returns = data.total_number_of_returns
        self.scanlines = [Scanline(scanline) for scanline in data.scanlines]
        self.packed = Packed(data.packed)
        self.algorithms = [Algorithm(algorithm) for algorithm in data.algorithms]
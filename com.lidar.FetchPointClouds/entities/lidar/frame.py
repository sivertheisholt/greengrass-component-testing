from entities.lidar.packed import Packed
from entities.lidar.algorithm import Algorithm
from entities.lidar.scan_pattern import ScanPattern
from entities.lidar.scanline import Scanline

class Frame:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.start_time_ns = data.get("start_time_ns")
        self.scan_pattern = ScanPattern(data.get("scan_pattern"))
        self.is_ramp_up_phase = data.get("is_ramp_up_phase")
        self.total_number_of_points = data.get("total_number_of_points")
        self.total_number_of_returns = data.get("total_number_of_returns")
        self.scanlines = [Scanline(scanline) for key, scanline in data.get("scanlines").items()]
        self.packed = Packed(data.get("packed"))
        self.algorithms = Algorithm(data.get("algorithm"))
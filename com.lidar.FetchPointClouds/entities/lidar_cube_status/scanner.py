from entities.lidar_cube_frame.scan_pattern import ScanPattern

class Scanner:
    def __init__(self, data: dict):
        self.state = data.state
        self.scan_pattern = ScanPattern(data.scan_pattern)

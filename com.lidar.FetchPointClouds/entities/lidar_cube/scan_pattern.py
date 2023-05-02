from entities.lidar_cube.horizontal import Horizontal
from entities.lidar_cube.vertical import Vertical
from entities.lidar_cube.pulse import Pulse
from entities.lidar_cube.frame_rate import FrameRate
from entities.lidar_cube.filter import Filter
from entities.lidar_cube.constraint import Constraint

class ScanPattern:
    def __init__(self, data: dict) -> None:
        self.horizontal = Horizontal(data.horizontal)
        self.vertical = Vertical(data.vertical)
        self.pulse = Pulse(data.pulse)
        self.frame_rate = FrameRate(data.frame_rate)
        self.filter = Filter(data.filter)
        self.constraints = [Constraint(constraint) for key, constraint in data.constraints]
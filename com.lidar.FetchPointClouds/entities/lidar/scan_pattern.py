from entities.lidar.horizontal import Horizontal
from entities.lidar.vertical import Vertical
from entities.lidar.pulse import Pulse
from entities.lidar.frame_rate import FrameRate
from entities.lidar.filter import Filter
from entities.lidar.constraint import Constraint

class ScanPattern:
    def __init__(self, data: dict) -> None:
        self.horizontal = Horizontal(data.horizontal)
        self.vertical = Vertical(data.vertical)
        self.pulse = Pulse(data.pulse)
        self.frame_rate = FrameRate(data.frame_rate)
        self.filter = Filter(data.filter)
        self.constraints = [Constraint(constraint) for key, constraint in data.constraints]
from entities.lidar_cube_frame.horizontal import Horizontal
from entities.lidar_cube_frame.vertical import Vertical
from entities.lidar_cube_frame.pulse import Pulse
from entities.lidar_cube_frame.frame_rate import FrameRate
from entities.lidar_cube_frame.filter import Filter
from entities.lidar_cube_frame.constraint import Constraint

class ScanPattern:
    def __init__(self, data: dict) -> None:
        self.horizontal = Horizontal(data.horizontal)
        self.vertical = Vertical(data.vertical)
        self.pulse = Pulse(data.pulse)
        self.frame_rate = FrameRate(data.frame_rate)
        self.filter = Filter(data.filter)
        self.constraints = [Constraint(constraint) for key, constraint in data.constraints]
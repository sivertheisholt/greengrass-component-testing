from entities.lidar.return_obj import Return
from entities.lidar.direction import Direction

class Point:
    def __init__(self, data: dict) -> None:
        self.id = data.id
        self.returns = [Return(return_obj) for return_obj in data.returns]
        self.start_offset_ns = data.start_offset_ns
        self.ambient_light_level = data.ambient_light_level
        self.direction = Direction(data.direction)
        self.channel_id = data.channel_id
        self.error_flags = data.error_flags
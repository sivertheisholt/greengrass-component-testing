from entities.lidar.return_obj import Return
from entities.lidar.direction import Direction

class Point:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.returns = [Return(return_obj) for key, return_obj in data.get("returns").items()]
        self.start_offset_ns = data.get("start_offset_ns")
        self.ambient_light_level = data.get("ambient_light_level")
        self.direction = Direction(data.get("direction"))
        self.channel_id = data.get("channel_id")
        self.error_flags = data.get("error_flags")
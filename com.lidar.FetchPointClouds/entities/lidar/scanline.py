from entities.lidar.point import Point

class Scanline:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.frame_id = data.get("frame_id")
        self.points = [Point(point) for key, point in data.get("points").items()]
        self.start_offset_ns = data.get("start_offset_ns")
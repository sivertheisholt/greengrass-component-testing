from entities.lidar_cube_frame.point import Point

class Scanline:
    def __init__(self, data: dict):
        self.id = data.id
        self.frame_id = data.frame_id
        self.points = [Point(point) for point in data.points]
        self.start_offset_ns = data.start_offset_ns
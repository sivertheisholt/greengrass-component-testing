class Packed:
    def __init__(self, data: dict) -> None:
        self.length = data.length
        self.cartesian = data.cartesian
        self.direction = data.direction
        self.range = data.range
        self.intensity = data.intensity
        self.ambient_light_level = data.ambient_light_level
        self.start_offset_ns = data.start_offset_ns
        self.point_id = data.point_id
        self.channel_id = data.channel_id
        self.return_id = data.return_id
class Packed:
    def __init__(self, data: dict) -> None:
        self.length = data.get("length")
        self.cartesian = data.get("cartesian")
        self.direction = data.get("direction")
        self.range = data.get("range")
        self.intensity = data.get("intensity")
        self.ambient_light_level = data.get("ambient_light_level")
        self.start_offset_ns = data.get("start_offset_ns")
        self.point_id = data.get("point_id")
        self.channel_id = data.get("channel_id")
        self.return_id = data.get("return_id")
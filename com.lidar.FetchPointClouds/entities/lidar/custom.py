class Custom:
    def __init__(self, data: dict) -> None:
        self.angle_trigger = data.get("angle_trigger")
        self.point_trigger = data.get("point_trigger")
        self.duration = data.get("duration")
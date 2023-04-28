from entities.lidar.custom import Custom

class Pulse:
    def __init__(self, data: dict) -> None:
        self.angle_Spacing = data.get("angle_Spacing")
        self.type = data.get("type")
        self.frame_mode = data.get("frame_mode")
        self.distortion_correction = data.get("distortion_correction")
        self.custom = Custom(data.get("custom"))
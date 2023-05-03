from entities.lidar_cube_frame.custom import Custom

class Pulse:
    def __init__(self, data: dict) -> None:
        self.angle_Spacing = data.angle_spacing
        self.type = data.type
        self.frame_mode = data.frame_mode
        self.distortion_correction = data.distortion_correction
        self.custom = Custom(data.custom)
from entities.lidar_cube_frame.field import Field

class Polynomial:
    def __init__(self, data: dict) -> None:
        self.reference = Field(data.reference)
        self.minimum = data.minimum
        self.maximum = data.maximum
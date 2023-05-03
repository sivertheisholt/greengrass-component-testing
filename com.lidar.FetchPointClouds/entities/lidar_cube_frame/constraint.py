from entities.lidar_cube_frame.field import Field
from entities.lidar_cube_frame.constant import Constant
from entities.lidar_cube_frame.polynomial import Polynomial

class Constraint:
    def __init__(self, data: dict) -> None:
        self.target = Field(data.target)
        self.reason = data.reason
        self.constant = Constant(data.constant)
        self.polynomial = Polynomial(data.polynomial)
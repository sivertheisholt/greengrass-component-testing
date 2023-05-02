from entities.lidar_cube.field import Field
from entities.lidar_cube.constant import Constant
from entities.lidar_cube.polynomial import Polynomial

class Constraint:
    def __init__(self, data: dict) -> None:
        self.target = Field(data.get("target"))
        self.reason = data.get("reason")
        self.constant = Constant(data.get("constant"))
        self.polynomial = Polynomial(data.get("polynomial"))
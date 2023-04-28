from entities.lidar.field import Field
from entities.lidar.constant import Constant
from entities.lidar.polynomial import Polynomial

class Constraint:
    def __init__(self, data: dict) -> None:
        self.target = Field(data.get("target"))
        self.reason = data.get("reason")
        self.constant = Constant(data.get("constant"))
        self.polynomial = Polynomial(data.get("polynomial"))
from entities.lidar.field import Field

class Polynomial:
    def __init__(self, data: dict) -> None:
        self.reference = Field(data.get("reference"))
        self.minimum = data.get("minimum")
        self.maximum = data.get("maximum")
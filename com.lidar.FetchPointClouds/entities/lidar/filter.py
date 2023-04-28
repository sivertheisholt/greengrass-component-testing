from entities.lidar.optional_value_range import OptionalValueRange
from entities.lidar.noise import Noise

class Filter:
    def __init__(self, data: dict) -> None:
        self.max_number_of_returns_per_point = data.get("max_number_of_returns_per_point")
        self.intensity = OptionalValueRange(data.get("intensity"))
        self.ambient_light_level = OptionalValueRange(data.get("ambient_light_level"))
        self.range = OptionalValueRange(data.get("range"))
        self.noise = Noise(data.get("noise"))
        self.delete_points_without_returns = data.get("delete_points_without_returns")
from entities.lidar_cube.optional_value_range import OptionalValueRange
from entities.lidar_cube.noise import Noise

class Filter:
    def __init__(self, data: dict) -> None:
        self.max_number_of_returns_per_point = data.max_number_of_returns_per_point
        self.intensity = OptionalValueRange(data.intensity)
        self.ambient_light_level = OptionalValueRange(data.ambient_light_level)
        self.range = OptionalValueRange(data.range)
        self.noise = Noise(data.noise)
        self.delete_points_without_returns = data.delete_points_without_returns
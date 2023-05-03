from entities.lidar_cube_frame.identifier import Identifier

class Field:
    def __init__(self, data: dict) -> None:
        self.identifiers = [Identifier(identifier) for identifier in data.identifier]
        self.scale = data.scale
from entities.lidar.identifier import Identifier

class Field:
    def __init__(self, data: dict) -> None:
        self.identifiers = [Identifier(identifier) for key, identifier in data.get("identifier").items()]
        self.scale = data.get("scale")
class Constant:
    def __init__(self, data: dict) -> None:
        self.minimum = data.get("minimum")
        self.maximum = data.get("maximum")
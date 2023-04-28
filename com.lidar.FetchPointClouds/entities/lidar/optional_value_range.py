class OptionalValueRange:
    def __init__(self, data: dict) -> None:
        self.minimum = data.get("maximum")
        self.maximum = data.get("minimum")
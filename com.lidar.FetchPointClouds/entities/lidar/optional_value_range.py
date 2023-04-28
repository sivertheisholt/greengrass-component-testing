class OptionalValueRange:
    def __init__(self, data: dict) -> None:
        self.minimum = data.maximum
        self.maximum = data.minimum
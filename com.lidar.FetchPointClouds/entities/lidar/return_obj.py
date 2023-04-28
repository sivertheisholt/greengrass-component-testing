class Return:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.cartesian = data.get("cartesian")
        self.range = data.get("range")
        self.intensity = data.get("intensity")
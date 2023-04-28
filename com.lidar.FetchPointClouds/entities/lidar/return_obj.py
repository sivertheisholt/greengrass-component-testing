class Return:
    def __init__(self, data: dict) -> None:
        self.id = data.id
        self.cartesian = data.cartesian
        self.range = data.range
        self.intensity = data.intensity
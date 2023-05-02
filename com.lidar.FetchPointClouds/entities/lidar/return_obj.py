class Return:
    def __init__(self, data: dict):
        self.id = data.id
        self.cartesian = [cartesian for cartesian in data.cartesian]
        self.range = data.range
        self.intensity = data.intensity
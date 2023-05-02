class Direction:
    def __init__(self, data: dict):
        self.azimuth = data.azimuth
        self.elevation = data.elevation
        self.origin = data.origin
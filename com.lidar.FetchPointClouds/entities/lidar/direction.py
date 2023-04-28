class Direction:
    def __init__(self, data: dict) -> None:
        self.azimuth = data.get("azimuth")
        self.elevation = data.get("elevation")
        self.origin = data.get("origin")
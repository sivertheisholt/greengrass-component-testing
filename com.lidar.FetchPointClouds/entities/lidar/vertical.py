class Vertical:
    def __init__(self, data: dict) -> None:
        self.fov = data.get("fov")
        self.scanlines_up = data.get("scanlines_up")
        self.scanlines_down = data.get("scanlines_down")
class Vertical:
    def __init__(self, data: dict) -> None:
        self.fov = data.fov
        self.scanlines_up = data.scanlines_up
        self.scanlines_down = data.scanlines_down
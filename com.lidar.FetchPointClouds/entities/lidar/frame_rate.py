class FrameRate:
    def __init__(self, data: dict) -> None:
        self.target = data.get("target")
        self.maximum = data.get("maximum")
        self.reference_time_offset = data.get("reference_time_offset")
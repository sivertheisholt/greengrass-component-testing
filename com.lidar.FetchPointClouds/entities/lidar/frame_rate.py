class FrameRate:
    def __init__(self, data: dict) -> None:
        self.target = data.target
        self.maximum = data.maximum
        self.reference_time_offset = data.reference_time_offset
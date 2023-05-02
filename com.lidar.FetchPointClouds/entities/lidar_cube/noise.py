class Noise:
    def __init__(self, data: dict) -> None:
        self.offset = data.offset
        self.gain = data.gain
        self.enable = data.enable
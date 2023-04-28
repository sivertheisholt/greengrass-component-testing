class Noise:
    def __init__(self, data: dict) -> None:
        self.offset = data.get("offset")
        self.gain = data.get("gain")
        self.enable = data.get("enable")
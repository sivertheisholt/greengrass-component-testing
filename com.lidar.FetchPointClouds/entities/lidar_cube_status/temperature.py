class Temperature:
    def __init__(self, data: dict):
        self.sensor = data.sensor
        self.value = data.value
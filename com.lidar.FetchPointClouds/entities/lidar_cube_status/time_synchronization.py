class TimeSynchronization:
    def __init__(self, data: dict):
        self.state = data.state
        self.offset_from_master = data.offset_from_master
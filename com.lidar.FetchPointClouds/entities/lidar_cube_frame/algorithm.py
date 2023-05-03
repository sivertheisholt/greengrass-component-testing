class Algorithm:
        def __init__(self, data: dict) -> None:
                self.background_subtraction = data.background_subtraction
                self.neighbor_filter = data.neighbor_filter
                self.static_transformation = data.static_transformation
                self.execution_time = data.execution_time
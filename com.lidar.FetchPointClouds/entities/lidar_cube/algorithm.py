class Algorithm:
        def __init__(self, data: dict) -> None:
                self.background_subtraction = data.get("background_subtraction")
                self.neighbor_filter = data.get("neighbor_filter")
                self.static_transformation = data.get("static_transformation")
                self.execution_time = data.get("execution_time")
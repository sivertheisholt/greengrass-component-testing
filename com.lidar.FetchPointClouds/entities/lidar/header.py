class Header:
    def __init__(self, data: dict) -> None:
        self.legacy_cube_serial_number = data.get("legacy_cube_serial_number")
        self.cube_serial_number = data.get("cube_serial_number")
        self.start_time_ns = data.get("start_time_ns")
        self.firmware_version = data.get("firmware_version")
        self.hardware_variant = data.get("hardware_variant")
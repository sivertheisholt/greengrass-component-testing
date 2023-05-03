class Identifier:
    def __init__(self, data: dict) -> None:
        self.id = data.id
        self.key = data.key
        self.camelcase_key = data.camelcase_key
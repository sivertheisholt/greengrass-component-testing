class Identifier:
    def __init__(self, data: dict) -> None:
        self.id = data.get("id")
        self.key = data.get("key")
        self.camelcase_key = data.get("camelcase_key")
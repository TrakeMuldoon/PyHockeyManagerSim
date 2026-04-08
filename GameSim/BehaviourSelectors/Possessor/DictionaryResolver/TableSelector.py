class TableSelector(dict):
    def __init__(self, level_name: str):
        super().__init__()
        self.level_name = level_name

    def __missing__(self, key):
        if key == "*":
            raise KeyError("key not found")
        try:
            return self["*"]
        except KeyError:
            raise KeyError(key + " not found")

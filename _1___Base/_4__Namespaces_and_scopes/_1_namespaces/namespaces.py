from typing import Self


class Namespace:
    def __init__(self, name: str, parent: Self) -> None:
        self.name = name
        self.parent = parent
        self.siblings = None
        self.variables = None

class MoneyBox:
    def __init__(self, capacity: int) -> None:
        self.available = 0
        self.capacity = capacity

    def can_add(self, v: int) -> bool:
        return self.capacity - self.available >= v

    def add(self, v: int) -> None:
        if self.can_add(v):
            self.available += v

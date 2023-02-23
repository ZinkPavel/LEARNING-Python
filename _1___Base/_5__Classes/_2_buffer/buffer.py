class Buffer:
    def __init__(self) -> None:
        self.buffer = list()

    def add(self, *a: int) -> int:
        self.buffer.extend(a)

        for i in range(len(self.buffer) // 5):
            print(sum(self.buffer[i * 5 : (i + 1) * 5]))

        bound = len(self.buffer) // 5 * 5
        if len(self.buffer) >= 5:
            self.buffer = self.buffer[bound:]

    def get_current_part(self) -> list[int]:
        return self.buffer

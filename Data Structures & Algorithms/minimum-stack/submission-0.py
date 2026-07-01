class MinStack:
    def __init__(self):
        self.stack = []
        self.min_value = []          # lista simple, no MinStack()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_value:
            self.min_value.append(val)
        else:
            current_min = self.min_value[-1]
            self.min_value.append(min(current_min, val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]     # faltaba el return
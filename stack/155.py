class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min = float("inf")

    def push(self, x: int) -> None:
        self.min = min(self.min, x)
        self.s.append((x, self.min))

    def pop(self) -> None:
        res = self.s.pop()[0]

        if res == self.min:
            self.min = self.s[-1][1] if self.s else float("inf")

        return res

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]

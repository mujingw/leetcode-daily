from sortedcontainers import SortedDict


class MaxStack:

    def __init__(self):
        self.stack = []
        self.sd = SortedDict()

    def push(self, x: int) -> None:
        self.stack.append(x)

        if x not in self.sd:
            self.sd[x] = 1
        else:
            self.sd[x] += 1

    def pop(self) -> int:
        x = self.stack.pop()
        self.sd[x] -= 1

        if self.sd[x] == 0:
            del self.sd[x]

        return x

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.sd.peekitem()[0]

    def popMax(self) -> int:
        curr_max = self.peekMax()
        p = len(self.stack) - 1

        while p >= 0 and self.stack[p] != curr_max:
            p -= 1

        self.stack.pop(p)
        self.sd[curr_max] -= 1

        if self.sd[curr_max] == 0:
            del self.sd[curr_max]

        return curr_max

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

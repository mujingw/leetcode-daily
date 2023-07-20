from collections import defaultdict
from itertools import accumulate


class MyCalendarTwo:

    def __init__(self):
        self.d = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.d[start] += 1
        self.d[end] -= 1

        ok = all(x < 3 for x in accumulate(self.d[t] for t in sorted(self.d.keys())))

        if not ok:
            self.d[start] -= 1
            self.d[end] += 1

        return ok

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start, end)

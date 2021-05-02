from collections import defaultdict
from itertools import accumulate


class MyCalendar:

    def __init__(self):
        self.d = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.d[start] += 1
        self.d[end] -= 1

        ok = all(x < 2 for x in accumulate(self.d[t] for t in sorted(self.d.keys())))

        if ok:
            return True
        else:
            self.d[start] -= 1
            self.d[end] += 1

            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start, end)

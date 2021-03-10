from itertools import accumulate

from sortedcontainers import SortedDict


class MyCalendarThree:

    def __init__(self):
        self.sd = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.sd[start] = self.sd[start] + 1 if start in self.sd else 1
        self.sd[end] = self.sd[end] - 1 if end in self.sd else -1

        return max(accumulate(self.sd[x] for x in self.sd.keys()))

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

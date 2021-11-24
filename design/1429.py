from collections import OrderedDict
from typing import List


class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique = OrderedDict()
        self.seen = set()

        for x in nums:
            self.add(x)

    def showFirstUnique(self) -> int:
        for key in self.unique.keys():
            return key

        return -1

    def add(self, value: int) -> None:
        if value not in self.seen:
            self.seen.add(value)
            self.unique[value] = 1
        else:
            if value in self.unique:
                del self.unique[value]

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

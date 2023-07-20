from random import randint
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        res, count = -1, 0

        for i, v in enumerate(self.nums):
            if v == target:
                count += 1
                chance = randint(1, count)

                if chance == count:
                    res = i

        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

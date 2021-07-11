from itertools import accumulate
from random import uniform
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.w_sum = list(accumulate(w))

    def pickIndex(self) -> int:
        target = uniform(0, self.w_sum[-1])
        left, right = 0, len(self.w_sum)

        while left < right:
            mid = (left + right) // 2

            if self.w_sum[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

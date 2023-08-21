from math import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def ok(divisor):
            total = sum(int(ceil(num / divisor)) for num in nums)

            return total <= threshold

        l, r = 1, max(nums) + 1

        while l < r:
            mid = (l + r) // 2

            if ok(mid):
                r = mid
            else:
                l = mid + 1

        return l

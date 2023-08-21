from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 10 ** 13

        while l < r:
            mid = (l + r) // 2

            if sum(ceil(p / mid) for p in piles) <= h:
                r = mid
            else:
                l = mid + 1

        return l

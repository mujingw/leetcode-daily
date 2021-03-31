from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def ok(k):
            hours = 0

            for pile in piles:
                time_taken, leftover = divmod(pile, k)
                hours += time_taken

                if leftover > 0:
                    hours += 1

            return hours <= h

        l, r = 1, 10 ** 13 + 1

        while l < r:
            mid = (l + r) // 2

            if ok(mid):
                r = mid
            else:
                l = mid + 1

        return l

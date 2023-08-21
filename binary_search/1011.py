from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def ok(capacity):
            days_needed = 1
            weight = 0

            for w in weights:
                if weight + w <= capacity:
                    weight += w
                else:
                    days_needed += 1
                    weight = w

            return days_needed <= D

        l, r = max(weights), 25 * (10 ** 6) + 1

        while l < r:
            mid = (l + r) // 2

            if ok(mid):
                r = mid
            else:
                l = mid + 1

        return l

from math import ceil
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def ok(speed, allowed):
            res = 0

            for d in dist[:-1]:
                res += ceil(d / speed)

            res += dist[-1] / speed

            return res <= allowed

        if hour <= len(dist) - 1:
            return -1

        l, r = 1, int(10e9)

        while l < r:
            mid = (l + r) // 2

            if ok(mid, hour):
                r = mid
            else:
                l = mid + 1

        return l

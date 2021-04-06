from math import ceil
from typing import List


class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        def ok(dist):
            stations_added = 0

            for a, b in zip(stations, stations[1:]):
                stations_added += (ceil((b - a) / dist) - 1)

            return stations_added > K

        DELTA = 1e-6
        l, r = 1e-6, stations[-1] - stations[0]

        while l + DELTA < r:
            mid = (l + r) / 2

            if ok(mid):
                l = mid + DELTA
            else:
                r = mid

        return l

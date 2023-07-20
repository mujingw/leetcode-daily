from collections import defaultdict
from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], to_be_removed: List[int]) -> List[List[int]]:
        res = []
        running_total = 0
        curr_start = None
        d = defaultdict(int)
        d[to_be_removed[0]] -= 1
        d[to_be_removed[1]] += 1

        for s, e in intervals:
            d[s] += 1
            d[e] -= 1

        for point in sorted(d.keys()):
            running_total += d[point]

            if curr_start is None and running_total > 0:
                curr_start = point
            elif curr_start is not None and running_total <= 0:
                res.append([curr_start, point])
                curr_start = None

        return res

from collections import defaultdict
from typing import List


class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        if not first or not second:
            return []

        d = defaultdict(int)
        total = 0
        curr_start = None
        res = []

        for s, e in first + second:
            d[s] += 1
            d[e] -= 1

        for p in sorted(d.keys()):
            total += d[p]

            if d[p] == 0:
                res.append([p, p])
            elif curr_start is None and total == 2:
                curr_start = p
            elif curr_start is not None and total < 2:
                res.append([curr_start, p])
                curr_start = None

        return res

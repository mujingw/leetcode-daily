from collections import defaultdict
from typing import List


class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(int)
        res = []
        agg = 0

        for a, b in l1 + l2:
            d[a] += 1
            d[b] -= 1

        for x in sorted(d.keys()):
            prev = agg
            agg += d[x]

            if prev < 2 and agg == 2:
                res.append([x, x])
            elif prev == 2 and agg < 2:
                res[-1][-1] = x
            elif prev == 1 and agg == 1:
                res.append([x, x])

        return res

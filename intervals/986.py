from typing import List


class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        points = []
        agg = 0
        res = []

        for a, b in first + second:
            points.append((a, 0))
            points.append((b, 1))

        for x, mark in sorted(points):
            if mark == 0:
                agg += 1

            if mark == 1:
                agg -= 1

            if agg > 1:
                res.append([x, x])
            elif agg == 1 and mark == 1:
                res[-1][-1] = x

        return res

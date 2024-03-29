from bisect import bisect
from collections import defaultdict, deque
from typing import List


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def total_width_after_merge(itvls):
            sorted_intervals = sorted(itvls + [[float("inf"), float("inf")]])
            s, e = sorted_intervals[0][0], sorted_intervals[0][1]
            res = []

            for cs, ce in sorted_intervals[1:]:
                if cs > e:
                    res.append([s, e])
                    s, e = cs, ce
                else:
                    e = max(ce, e)

            return sum(e - s for s, e in res)

        total_area = 0
        MOD = 10 ** 9 + 7
        y2x_itvls = defaultdict(deque)

        for x1, y1, x2, y2 in rectangles:
            if y1 != y2:
                bisect.insort(y2x_itvls[y1], (1, x1, x2))
                bisect.insort(y2x_itvls[y2], (-1, x1, x2))

        sorted_yvals = sorted(y2x_itvls.keys())
        prev_y = sorted_yvals[0]
        active_itvls = []

        for y in sorted_yvals:
            while y2x_itvls[y]:
                typ, xs, xe = y2x_itvls[y].popleft()
                height = y - prev_y
                total_area += (total_width_after_merge(active_itvls) * height)

                if typ == 1:
                    active_itvls.append([xs, xe])
                else:
                    active_itvls.remove([xs, xe])

                prev_y = y

        return total_area % MOD

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals + [[float("inf"), float("inf")]])
        s, e = sorted_intervals[0][0], sorted_intervals[0][1]
        res = []

        for cs, ce in sorted_intervals[1:]:
            if cs > e:
                res.append([s, e])
                s, e = cs, ce
            else:
                e = max(ce, e)

        return res

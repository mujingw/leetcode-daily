from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        all_intervals = intervals + [new_interval, [float("inf"), float("inf")]]
        all_intervals.sort()
        s, e = all_intervals[0][0], all_intervals[0][1]
        res = []

        for cs, ce in all_intervals[1:]:
            if cs > e:
                res.append([s, e])
                s, e = cs, ce
            else:
                e = max(ce, e)

        return res

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        covered = 0
        my_intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        s, e = my_intervals[0][0], my_intervals[0][1]

        for cs, ce in my_intervals[1:]:
            if cs >= s and ce <= e:
                covered += 1
            else:
                s, e = cs, ce

        return len(intervals) - covered

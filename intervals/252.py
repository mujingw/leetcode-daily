from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort()
        s, e = intervals[0]

        for cs, ce in intervals[1:]:
            if cs < e:
                return False
            else:
                s, e = cs, ce

        return True

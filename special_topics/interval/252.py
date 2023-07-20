from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        d = defaultdict(int)

        for s, e in intervals:
            d[s] += 1
            d[e] -= 1

        return all(x <= 1 for x in accumulate(d[t] for t in sorted(d.keys())))

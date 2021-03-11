from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        d = defaultdict(int)

        for s, e in intervals:
            d[s] += 1
            d[e] -= 1

        return max(accumulate(d[t] for t in sorted(d.keys())))

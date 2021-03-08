from heapq import heappush, heapreplace
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h = []

        for s, e in intervals:
            if not h:
                heappush(h, e)
            else:
                if s < h[0]:
                    heappush(h, e)
                else:
                    heapreplace(h, e)

        return len(h)

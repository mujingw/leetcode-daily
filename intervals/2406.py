from collections import defaultdict
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        rooms = defaultdict(int)
        res = 0
        running = 0

        for s, e in intervals:
            rooms[s] += 1
            rooms[e + 0.1] -= 1

        for x in sorted(rooms.keys()):
            running += rooms[x]
            res = max(res, running)

        return res

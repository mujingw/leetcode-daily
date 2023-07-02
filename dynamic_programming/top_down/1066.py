from functools import lru_cache
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        self.workers = workers
        self.bikes = bikes

        return self.backtrack(0, 0)

    @lru_cache(None)
    def backtrack(self, wid, used):
        if wid == len(self.workers):
            return 0

        res = float('inf')

        for i in range(len(self.bikes)):
            mask = 1 << i

            if mask & used != 0:
                continue

            used |= mask
            dist = abs(self.bikes[i][0] - self.workers[wid][0]) + abs(self.bikes[i][1] - self.workers[wid][1])
            res = min(res, dist + self.backtrack(wid + 1, used))
            used &= ~mask

        return res

from functools import lru_cache
from itertools import accumulate
from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        self.piles = piles
        self.presums = [list(accumulate(pile)) for pile in piles]

        return self.backtrack(0, k)

    @lru_cache(None)
    def backtrack(self, idx, k):
        if idx == len(self.piles) or k == 0:
            return 0

        res = self.backtrack(idx + 1, k)

        for d in range(min(k, len(self.piles[idx]))):
            res = max(res, self.backtrack(idx + 1, k - d - 1) + self.presums[idx][d])

        return res

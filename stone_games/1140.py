from functools import lru_cache
from itertools import accumulate
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.N = len(piles)
        self.total = sum(piles)
        self.presum = [0] + list(accumulate(piles))

        return (self.total + self.max_diff(0, 1)) // 2

    @lru_cache(None)
    def max_diff(self, pos, M):
        if pos >= self.N:
            return 0

        diff = float('-inf')

        for x in range(1, min(2 * M + 1, self.N - pos + 1)):
            diff = max(
                diff,
                self.presum[pos + x] - self.presum[pos] - self.max_diff(pos + x, max(M, x)))

        return diff

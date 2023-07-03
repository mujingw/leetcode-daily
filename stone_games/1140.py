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

        for i in range(2 * M):
            if pos + i + 1 > self.N:
                break

            diff = max(
                diff,
                self.presum[pos + i + 1] - self.presum[pos] - self.max_diff(pos + i + 1, max(M, i + 1)))

        return diff

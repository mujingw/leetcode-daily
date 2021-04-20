from functools import lru_cache
from typing import List


class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        @lru_cache(None)
        def helper(target, nums_needed, pos):
            if nums_needed == 0:
                return target == 0

            if target < 0 or nums_needed + pos > N:
                return False

            return helper(target - A[pos], nums_needed - 1, pos + 1) or \
                   helper(target, nums_needed, pos + 1)

        N, total = len(A), sum(A)

        for nums_needed in range(1, N // 2 + 1):
            if total * nums_needed % N == 0:
                if helper(total * nums_needed // N, nums_needed, 0):
                    return True

        return False

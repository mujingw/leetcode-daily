from collections import defaultdict
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l, r = 0, 0
        window = defaultdict(int)
        res = 0

        while r < len(A):
            window[A[r]] += 1
            r += 1

            while window[0] > K:
                window[A[l]] -= 1
                l += 1

            res = max(res, r - l)

        return res

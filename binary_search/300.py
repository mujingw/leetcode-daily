from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cand = []

        for v in nums:
            idx = bisect_left(cand, v)

            if idx == len(cand):
                cand.append(v)
            else:
                cand[idx] = v

        return len(cand)

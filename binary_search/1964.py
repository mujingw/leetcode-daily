from bisect import bisect_right
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: List[int]) -> List[int]:
        cand, res = [], []

        for x in nums:
            idx = bisect_right(cand, x)
            res.append(idx + 1)

            if idx == len(cand):
                cand.append(x)
            else:
                cand[idx] = x

        return res

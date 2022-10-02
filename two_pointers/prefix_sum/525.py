from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        res, total = 0, 0

        for i, v in enumerate(nums):
            if v == 0:
                total += 1
            else:
                total -= 1

            if total not in d:
                d[total] = i
            else:
                res = max(res, i - d[total])

        return res

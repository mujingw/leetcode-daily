from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        presum = {0: -1}
        running = 0
        res = 0

        for i, v in enumerate(nums):
            running += v
            needed = running - k

            if needed in presum:
                res = max(res, i - presum[needed])

            if running not in presum:
                presum[running] = i

        return res

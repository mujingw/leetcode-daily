from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = defaultdict(int)
        presum[0] = 1
        res = 0
        total = 0

        for x in nums:
            total += x
            res += presum[total - k]
            presum[total] += 1

        return res

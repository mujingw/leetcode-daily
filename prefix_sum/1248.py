from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        presum = defaultdict(int)
        presum[0] = 1
        odd_count = 0
        res = 0

        for i, num in enumerate(nums):
            odd_count += (num % 2)
            res += presum[odd_count - k]
            presum[odd_count] += 1

        return res

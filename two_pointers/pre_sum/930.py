from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        presum = defaultdict(int)
        presum[0] = 1
        sum_so_far = 0
        res = 0

        for num in A:
            sum_so_far += num
            res += presum[sum_so_far - S]
            presum[sum_so_far] += 1

        return res

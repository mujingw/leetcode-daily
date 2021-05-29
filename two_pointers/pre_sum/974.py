from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        presum = defaultdict(int)
        presum[0] = 1
        res = 0
        sum_so_far = 0

        for i, v in enumerate(A):
            sum_so_far += v
            sum_so_far %= K
            res += presum[sum_so_far]
            presum[sum_so_far] += 1

        return res

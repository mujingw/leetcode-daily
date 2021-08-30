from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ab, cd = defaultdict(int), defaultdict(int)
        res = 0

        for a, b in product(nums1, nums2):
            ab[a + b] += 1

        for c, d in product(nums3, nums4):
            cd[c + d] += 1

        for v in ab:
            if -v in cd:
                res += (ab[v] * cd[-v])

        return res

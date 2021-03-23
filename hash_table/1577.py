from collections import defaultdict
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N1, N2 = len(nums1), len(nums2)
        res = 0
        nums1_multiply = defaultdict(int)
        nums2_multiply = defaultdict(int)

        for i in range(N1):
            for j in range(i + 1, N1):
                nums1_multiply[nums1[i] * nums1[j]] += 1

        for i in range(N2):
            for j in range(i + 1, N2):
                nums2_multiply[nums2[i] * nums2[j]] += 1

        for a in nums1:
            res += nums2_multiply[a * a]

        for a in nums2:
            res += nums1_multiply[a * a]

        return res

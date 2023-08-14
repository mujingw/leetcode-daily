from collections import defaultdict
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(lambda: -1)
        stack = []

        for i, v in enumerate(nums2):
            while stack and nums2[stack[-1]] < v:
                k = nums2[stack.pop()]
                d[k] = v

            stack.append(i)

        return [d[k] for k in nums1]

from collections import defaultdict
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res, stack, mapping = [], [], defaultdict(lambda: -1)

        for x in nums2:
            while stack and x > stack[-1]:
                mapping[stack.pop()] = x

            stack.append(x)

        return [mapping[x] for x in nums1]

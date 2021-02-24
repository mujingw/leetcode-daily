from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s, lookup, res = [], {}, []

        for num in nums2:
            while s and s[-1] < num:
                lookup[s.pop()] = num

            s.append(num)

        return [lookup[num] if num in lookup else -1 for num in nums1]

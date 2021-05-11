from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l, r = -1, -1

        for i, (a, b) in enumerate(zip(nums, sorted(nums))):
            if a != b:
                r = i

                if l == -1:
                    l = i

        return r - l + 1 if r != -1 and l != -1 else 0

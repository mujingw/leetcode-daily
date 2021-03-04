from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        circular = nums + nums
        s = []
        res = [-1] * len(nums)

        for i, v in enumerate(circular):
            while s and s[-1][0] < v:
                val, idx = s.pop()
                res[idx] = v

            s.append((v, i % len(nums)))

        return res

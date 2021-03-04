from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        N = len(nums)

        for i, v in enumerate(nums):
            nums_left_including_v = N - i

            while s and s[-1] > v and len(s) - 1 + nums_left_including_v >= k:
                s.pop()

            s.append(v)

        return s[:k]

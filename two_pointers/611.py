from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        res = 0

        for i in range(N - 1, 1, -1):
            l, r = 0, i - 1

            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += (r - l)
                    r -= 1
                else:
                    l += 1

        return res

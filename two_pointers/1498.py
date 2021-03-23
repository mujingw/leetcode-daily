from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD, N = 10 ** 9 + 7, len(nums)
        res = 0
        nums.sort()
        l, r = 0, N - 1

        while l <= r:
            if nums[l] + nums[r] <= target:
                gap = r - l
                res += (2 ** gap)
                l += 1
            else:
                r -= 1

        return res % MOD

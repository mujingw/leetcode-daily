from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        last_good_pos = N - 1

        for start_at in range(N - 2, -1, -1):
            if start_at + nums[start_at] >= last_good_pos:
                last_good_pos = start_at

        return last_good_pos == 0

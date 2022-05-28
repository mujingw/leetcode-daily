from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        dp_up = [1] * N
        dp_down = [1] * N

        for i in range(1, N):
            if nums[i - 1] < nums[i]:
                dp_up[i] = dp_up[i - 1]
                dp_down[i] = dp_up[i - 1] + 1
            elif nums[i - 1] > nums[i]:
                dp_up[i] = dp_down[i - 1] + 1
                dp_down[i] = dp_down[i - 1]
            else:
                dp_up[i] = dp_up[i - 1]
                dp_down[i] = dp_down[i - 1]

        return max(dp_down[-1], dp_up[-1])

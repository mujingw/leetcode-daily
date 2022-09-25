from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        res = []
        left, right = [1] * N, [1] * N

        for i in range(1, N):
            if nums[i] <= nums[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right[i] = right[i + 1] + 1

        for i in range(k, N - k):
            if left[i - 1] >= k and right[i + 1] >= k:
                res.append(i)

        return res

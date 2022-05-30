from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        N = len(heights)
        res = 0
        left_max = [0] * N
        right_max = [0] * N
        left_max[0] = heights[0]
        right_max[-1] = heights[-1]

        for i in range(1, N):
            left_max[i] = max(heights[i], left_max[i - 1])

        for i in range(N - 2, -1, -1):
            right_max[i] = max(heights[i], right_max[i + 1])

        for i in range(1, N - 1):
            res += min(left_max[i], right_max[i]) - heights[i]

        return res

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        res = 0

        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] > v:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, w * h)

            stack.append(i)

        return res

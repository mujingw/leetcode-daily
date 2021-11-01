from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res, stack = [], []

        for i in range(len(heights) - 1, -1, -1):
            h = heights[i]

            if not stack or h > stack[-1]:
                res.append(i)
                stack.append(h)

        return res[::-1]

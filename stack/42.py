from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        N = len(heights)
        res = 0
        stack = []

        for i in range(N):
            while stack and heights[i] > heights[stack[-1]]:
                top = stack.pop()

                if not stack:
                    break

                dist = i - stack[-1] - 1
                h = min(heights[i], heights[stack[-1]]) - heights[top]
                res += (dist * h)

            stack.append(i)

        return res

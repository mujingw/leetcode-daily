from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        stack = []
        res, additional_water = 0, 0
        N = len(heights)
        curr_idx = 0

        while curr_idx < N:
            height = heights[curr_idx]

            if not stack:
                stack.append(curr_idx)
                curr_idx += 1
            elif height <= heights[stack[-1]]:
                stack.append(curr_idx)
                curr_idx += 1
            else:
                base_height_idx = stack.pop()

                if not stack:
                    additional_water = 0
                else:
                    h = min(heights[stack[-1]], height) - heights[base_height_idx]
                    w = curr_idx - stack[-1] - 1
                    additional_water = w * h

                res += additional_water

        return res

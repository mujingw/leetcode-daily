from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        res, lmax, rmax, l, r = 0, 0, 0, 0, len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                lmax = max(lmax, heights[l])
                res += lmax - heights[l]
                l += 1
            else:
                rmax = max(rmax, heights[r])
                res += rmax - heights[r]
                r -= 1

        return res

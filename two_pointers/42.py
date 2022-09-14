from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        lmax, rmax = heights[l], heights[r]

        while l < r:
            if heights[l] < heights[r]:
                if heights[l] >= lmax:
                    lmax = heights[l]
                else:
                    res += (lmax - heights[l])

                l += 1
            else:
                if heights[r] >= rmax:
                    rmax = heights[r]
                else:
                    res += (rmax - heights[r])

                r -= 1

        return res

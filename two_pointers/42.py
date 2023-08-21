from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res, lmax, rmax = 0, height[0], height[r]

        while l < r:
            if lmax < rmax:
                res += lmax - height[l]
                l += 1
                lmax = max(lmax, height[l])
            else:
                res += rmax - height[r]
                r -= 1
                rmax = max(rmax, height[r])

        res += (max(min(lmax, rmax), 0)  - height[l])

        return res

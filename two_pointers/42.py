from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        lmax, rmax = 0, 0
        l, r = 0, len(height) - 1

        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            if lmax < rmax:
                res += (lmax - height[l])
                l += 1
            else:
                res += (rmax - height[r])
                r -= 1

        return res

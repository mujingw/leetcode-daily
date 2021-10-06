class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0

        while x > 0 or y > 0:
            lsb_x, lsb_y = x & 1, y & 1
            res += (lsb_x ^ lsb_y)
            x >>= 1
            y >>= 1

        return res

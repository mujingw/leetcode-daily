class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0 and n & 1 != 1:
            n >>= 1

        return n == 1

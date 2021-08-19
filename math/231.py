class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 1 and n % 2 == 0:
            n //= 2

        return n == 1

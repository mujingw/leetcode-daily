from math import lcm


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        l, r = 1, 10 ** 10 + 1

        while l < r:
            mid = (l + r) // 2

            if self.ok(a, b, c, n, mid):
                l = mid + 1
            else:
                r = mid

        return l

    def ok(self, a, b, c, n, x):
        return x // a + x // b + x // c - x // lcm(a, b) - x // lcm(a, c) - x // lcm(b, c) + x // lcm(a, b, c) < n

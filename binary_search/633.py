from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def is_perfect_square(num: int) -> bool:
            l, r = 1, num

            while l < r:
                mid = (l + r) // 2

                if mid * mid == num:
                    return True
                elif mid * mid < num:
                    l = mid + 1
                else:
                    r = mid

            return l * l == num

        return c == 0 or any(is_perfect_square(c - a * a) for a in range(int(sqrt(c)) + 1))

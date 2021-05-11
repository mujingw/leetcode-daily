class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1

        positive = True

        if dividend > 0 > divisor:
            positive = False

        if dividend < 0 < divisor:
            positive = False

        res = 0
        dividend, divisor = abs(dividend), abs(divisor)

        while dividend >= divisor:
            deduction, count = divisor, 1

            while dividend >= deduction:
                dividend -= deduction
                res += count

                count <<= 1
                deduction <<= 1

        return res if positive else -res

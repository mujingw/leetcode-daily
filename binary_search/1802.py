class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def ok(idx, val, r_idx_incl):
            total = val
            ln = min(idx, val - 1)
            rn = min(r_idx_incl - idx, val - 1)
            l_fill = (idx - ln)
            r_fill = (r_idx_incl - idx - rn)
            left_sum = ((val - ln) * ln + (ln * (ln - 1) // 2))
            right_sum = ((val - 1) * rn - (rn * (rn - 1) // 2))
            total += (left_sum + right_sum + l_fill + r_fill)

            return total <= MAX

        MAX = maxSum
        l, r = 0, 10 ** 9 + 1

        while l < r:
            mid = (l + r) // 2

            if ok(index, mid, n - 1):
                l = mid + 1
            else:
                r = mid

        if ok(index, l, n - 1):
            return l
        else:
            return l - 1

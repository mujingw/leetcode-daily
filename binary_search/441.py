class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n

        while l < r:
            mid = (l + r) // 2

            if ((1 + mid) * mid // 2) > n:
                r = mid
            else:
                l = mid + 1

        return l if ((1 + l) * l // 2) == n else l - 1

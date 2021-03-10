from functools import lru_cache


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        @lru_cache(None)
        def helper(n, p):
            if n < 0:
                return False

            if n == 0:
                return True

            for i in range(p, 15):
                factor = 3 ** i

                if helper(n - factor, i + 1):
                    return True

        return helper(n, 0)

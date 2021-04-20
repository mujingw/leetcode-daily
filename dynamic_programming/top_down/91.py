from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        @lru_cache(None)
        def dfs(s, start, end):
            if start == end:
                return 1

            if s[start] == "0":
                return 0

            if end - start == 1:
                return 1

            ways = dfs(s, start + 1, end)

            if int(s[start:start + 2]) <= 26:
                ways += dfs(s, start + 2, end)

            return ways

        return dfs(s, 0, len(s))

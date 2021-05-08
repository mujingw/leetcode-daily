from functools import lru_cache
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N, DIR = len(arr), (-1, 1)

        @lru_cache(None)
        def dfs(pos):
            best = 0

            for di in DIR:
                for np in range(pos + di * 1, pos + di * d + di, di):
                    if 0 <= np < N and arr[pos] > arr[np]:
                        best = max(dfs(np), best)
                    else:
                        break

            return best + 1

        return max(dfs(i) for i in range(N))

from functools import lru_cache
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)
        DIR = (-1, 1)
        res = 0

        @lru_cache(None)
        def dfs(pos):
            best = 0

            for di in DIR:
                for next_pos in range(pos + di * 1, pos + di * d + di, di):
                    if 0 <= next_pos < N and arr[pos] > arr[next_pos]:
                        best = max(dfs(next_pos), best)
                    else:
                        break

            return best + 1

        for i in range(N):
            res = max(res, dfs(i))

        return res

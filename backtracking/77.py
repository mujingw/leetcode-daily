from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(res, curr, start, n, k):
            if len(curr) == k:
                res.append(curr[:])

                return

            for i in range(start, n + 1):
                curr.append(i)
                dfs(res, curr, i + 1, n, k)
                curr.pop()

        res = []
        dfs(res, [], 1, n, k)

        return res

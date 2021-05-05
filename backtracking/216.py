from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(res, curr, start, t):
            if len(curr) == k:
                if t == 0:
                    res.append(curr[:])

                return

            for i in range(start, 10):
                if t - i < 0:
                    continue

                curr.append(i)
                backtrack(res, curr, i + 1, t - i)
                curr.pop()

        res = []
        backtrack(res, [], 1, n)

        return res

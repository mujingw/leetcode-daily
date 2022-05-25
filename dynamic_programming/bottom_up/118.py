from typing import List


class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res = [[1] * r for r in range(1, n + 1)]

        for r in range(2, n):
            for c in range(1, r):
                res[r][c] = res[r - 1][c - 1] + res[r - 1][c]

        return res

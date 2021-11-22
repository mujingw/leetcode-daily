from itertools import product
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def calc(op, a, b):
            if op == '+':
                return a + b

            if op == '-':
                return a - b

            if op == '*':
                return a * b

        def dfs(s):
            if s.isdigit():
                return [int(s)]

            res = []

            for i, v in enumerate(s):
                if v in '+-*':
                    left, right = dfs(s[:i]), dfs(s[i + 1:])

                    for l, r in product(left, right):
                        res.append(calc(v, l, r))

            return res

        return dfs(expression)

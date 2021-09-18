from functools import lru_cache
from itertools import product
from typing import List


class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        def calc(a, b, op):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b

        @lru_cache(None)
        def helper(s):
            if s.isdigit():
                return [int(s)]

            res = []

            for i, ch in enumerate(s):
                if ch in "+-*":
                    left = helper(s[:i])
                    right = helper(s[i + 1:])
                    res.extend([calc(m, n, ch) for m, n in product(left, right)])

            return res

        return helper(s)

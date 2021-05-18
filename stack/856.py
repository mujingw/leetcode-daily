class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        layer = 0

        for a, b in zip(s, s[1:]):
            if a + b == '()':
                res += (2 ** layer)

            if a == '(':
                layer += 1
            else:
                layer -= 1

        return res

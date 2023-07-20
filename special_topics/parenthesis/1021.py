class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        level = 0

        for ch in s:
            if ch == ')':
                level -= 1

            res.append((ch, level))

            if ch == '(':
                level += 1

        return ''.join(ch for ch, level in res if level != 0)

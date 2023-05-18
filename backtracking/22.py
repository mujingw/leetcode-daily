from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, [], n, n)

        return res

    def backtrack(self, res, curr, left, right):
        if left == 0 and right == 0:
            res.append(''.join(curr))
            return

        if right < left or left < 0 or right < 0:
            return

        curr.append('(')
        self.backtrack(res, curr, left - 1, right)
        curr.pop()

        curr.append(')')
        self.backtrack(res, curr, left, right - 1)
        curr.pop()

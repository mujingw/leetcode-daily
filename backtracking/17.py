from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(res, curr, pos):
            if len(curr) == len(digits):
                res.append(''.join(curr))

                return

            for ch in PHONE[digits[pos]]:
                curr.append(ch)
                backtrack(res, curr, pos + 1)
                curr.pop()

        if not digits:
            return ''

        PHONE = {'2': 'abc', '3': 'def',
                 '4': 'ghi', '5': 'jkl', '6': 'mno',
                 '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        backtrack(res, [], 0)

        return res

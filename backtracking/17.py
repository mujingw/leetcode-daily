from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(res, curr, pos, digits, phone):
            if len(curr) == len(digits):
                res.append("".join(curr))
                return

            for ch in phone[digits[pos]]:
                dfs(res, curr + [ch], pos + 1, digits, phone)

        if not digits:
            return []

        phone = {"2": "abc", "3": "def",
                 "4": "ghi", "5": "jkl", "6": "mno",
                 "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        dfs(res, [], 0, digits, phone)

        return res

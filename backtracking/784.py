from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def backtrack(res, curr, pos):
            if pos == N:
                res.append(''.join(curr))

                return

            val = s[pos]
            curr.append(val)
            backtrack(res, curr, pos + 1)
            curr.pop()

            if val.isalpha():
                alt = val.upper() if val.islower() else val.lower()
                curr.append(alt)
                backtrack(res, curr, pos + 1)
                curr.pop()

        N = len(s)
        res = []
        backtrack(res, [], 0)

        return res

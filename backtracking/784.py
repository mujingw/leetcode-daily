from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(res, curr, pos):
            if len(curr) == len(S):
                res.append("".join(curr))

                return

            ch = S[pos]

            curr.append(ch)
            dfs(res, curr, pos + 1)
            curr.pop()

            if ch.isalpha():
                if ch.islower():
                    curr.append(ch.upper())
                else:
                    curr.append(ch.lower())

                dfs(res, curr, pos + 1)
                curr.pop()

        res = []
        dfs(res, [], 0)

        return res

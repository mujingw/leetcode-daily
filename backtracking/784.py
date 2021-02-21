from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def dfs(res, curr, S, start):
            if len(curr) == len(S):
                res.append("".join(curr))

                return

            for i in range(start, len(S)):
                curr.append(S[i])
                dfs(res, curr, S, i + 1)
                curr.pop()

                if S[i].isalpha():
                    if S[i].islower():
                        curr.append(S[i].upper())
                    else:
                        curr.append(S[i].lower())

                    dfs(res, curr, S, i + 1)
                    curr.pop()

        res = []
        dfs(res, [], S, 0)

        return res

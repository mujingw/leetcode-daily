from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(res, curr, s):
            if s:
                for i in range(1, len(s) + 1):
                    prefix = s[:i]

                    if prefix == prefix[::-1]:
                        curr.append(prefix)
                        dfs(res, curr, s[i:])
                        curr.pop()
            else:
                res.append(curr[:])

        res = []
        dfs(res, [], s)

        return res

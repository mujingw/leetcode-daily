from typing import List


class Solution:
    def wordBreak(self, s: str, wd: List[str]) -> List[str]:
        return self.helper(s, set(wd), {})

    def helper(self, s, wd, memo):
        if s in memo:
            return memo[s]

        res = []

        if s in wd:
            res.append(s)

        for i in range(1, len(s)):
            left = s[:i]

            if left in wd:
                for right in self.helper(s[i:], wd, memo):
                    res.append(left + " " + right)

        memo[s] = res

        return res

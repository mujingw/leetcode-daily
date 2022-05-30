from typing import List


class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        N = len(s)
        ws = set(word_dict)
        dp = [False for _ in range(N + 1)]
        dp[0] = True

        for end in range(N + 1):
            for start in range(end):
                if dp[start] and s[start:end] in ws:
                    dp[end] = True
                    break

        return dp[-1]

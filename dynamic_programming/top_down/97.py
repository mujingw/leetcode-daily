from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def dfs(i, j, k):
            if i == -1:
                return s2[:j + 1] == s3[:k + 1]
            elif j == -1:
                return s1[:i + 1] == s3[:k + 1]
            elif k == -1:
                return s1[:i + 1] == s2[:j + 1]
            else:
                return (s1[i] == s3[k] and dfs(i - 1, j, k - 1)) or (s2[j] == s3[k] and dfs(i, j - 1, k - 1))

        return dfs(len(s1) - 1, len(s2) - 1, len(s3) - 1)

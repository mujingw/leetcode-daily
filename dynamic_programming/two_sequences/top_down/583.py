from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def helper(l1, l2):
            if l1 == 0:
                return l2

            if l2 == 0:
                return l1

            if word1[l1 - 1] == word2[l2 - 1]:
                return helper(l1 - 1, l2 - 1)
            else:
                return min(helper(l1 - 1, l2), helper(l1, l2 - 1)) + 1

        return helper(len(word1), len(word2))

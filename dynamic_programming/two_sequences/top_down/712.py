from functools import lru_cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def helper(l1, l2):
            if l1 == 0:
                return sum([ord(ch) for ch in s2[:l2]])

            if l2 == 0:
                return sum([ord(ch) for ch in s1[:l1]])

            if s1[l1 - 1] == s2[l2 - 1]:
                return helper(l1 - 1, l2 - 1)
            else:
                return min(helper(l1 - 1, l2) + ord(s1[l1 - 1]), helper(l1, l2 - 1) + ord(s2[l2 - 1]))

        return helper(len(s1), len(s2))

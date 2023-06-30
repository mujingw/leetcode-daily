from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, left, seen = 0, 0, defaultdict(lambda: float('-inf'))

        for i, v in enumerate(s):
            left = max(left, seen[v] + 1)
            seen[v] = i
            res = max(res, i - left + 1)

        return res

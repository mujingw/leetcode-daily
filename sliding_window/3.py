class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res = 0, 0, 0
        seen = {}

        for i, ch in enumerate(s):
            if ch in seen:
                l = max(l, seen[ch] + 1)

            res = max(res, i - l + 1)
            seen[ch] = i

        return res

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        mask = 0
        d = {mask: -1}
        res = 0

        for i, ch in enumerate(s):
            if ch in "aeiou":
                mask ^= 1 << (ord(ch) - ord('a'))

            if mask not in d:
                d[mask] = i

            res = max(res, i - d[mask])

        return res

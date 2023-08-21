from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r, N = 0, 0, len(s)
        window = defaultdict(int)
        res = 0

        while r < N:
            window[s[r]] += 1
            r += 1

            while len(window) > 2:
                window[s[l]] -= 1

                if window[s[l]] == 0:
                    del window[s[l]]

                l += 1

            res = max(res, r - l)

        return res

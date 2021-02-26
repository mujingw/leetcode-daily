from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, r, N = 0, 0, len(s)
        window = defaultdict(int)
        res = 0

        while r < N:
            window[s[r]] += 1
            r += 1

            while len(window) < r - l:
                window[s[l]] -= 1

                if window[s[l]] == 0:
                    del window[s[l]]

                l += 1

            res = max(res, r - l)

        return res

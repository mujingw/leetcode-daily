from collections import defaultdict


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        def get_mask(window):
            res = 0
            lookup = {"a": 16, "e": 8, "i": 4, "o": 2, "u": 1}

            for ch, count in window.items():
                if ch in "aeiou" and count % 2 != 0:
                    res += lookup[ch]

            return res

        pre = defaultdict(list)
        pre[0].append(-1)
        res = 0
        window = defaultdict(int)

        for i, ch in enumerate(s):
            window[ch] += 1
            mask = get_mask(window)

            if mask in pre:
                res = max(res, i - pre[mask][0])

            pre[mask].append(i)

        return res

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, N = 0, 0, len(s)
        c = Counter()
        res = 0

        while r < N:
            c[s[r]] += 1
            r += 1
            max_count = c.most_common()[0][1]

            while r - l - max_count > k:
                c[s[l]] -= 1
                l += 1
                max_count = c.most_common()[0][1]

            res = max(res, r - l)

        return res

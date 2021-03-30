import collections


class Solution:
    def balancedString(self, s: str) -> int:
        N, D = len(s), len(s) // 4
        res, l, r = N, 0, 0
        c = collections.Counter(s)

        while r < N:
            c[s[r]] -= 1
            r += 1

            while l < N and all(v <= D for v in c.values()):
                res = min(res, r - l)
                c[s[l]] += 1
                l += 1

        return res

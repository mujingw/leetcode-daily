class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, r = 0, 0
        window = {c: 0 for c in "abc"}
        res = 0
        N = len(s)

        while r < N:
            window[s[r]] += 1
            r += 1

            while all(window.values()):
                res += (N - r + 1)
                window[s[l]] -= 1
                l += 1

        return res

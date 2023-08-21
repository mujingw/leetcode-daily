from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def char_count_equal(d1, d2):
            return all(d1[chr(ord('a') + i)] == d2[chr(ord('a') + i)] for i in range(26))

        M, N = len(s1), len(s2)
        l, r = 0, 0
        ref = defaultdict(int)
        window = defaultdict(int)

        for ch in s1:
            ref[ch] += 1

        while r < N:
            window[s2[r]] += 1
            r += 1

            if r - l > M:
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1

            if char_count_equal(ref, window):
                return True

        return False

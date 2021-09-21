from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r = 0, 0
        cs, cp = Counter(), Counter(p)
        res = []

        while r < len(s):
            right = s[r]
            r += 1
            cs[right] += 1

            if r - l == len(p):
                if cs == cp:
                    res.append(l)

                left = s[l]
                l += 1
                cs[left] -= 1

                if cs[left] == 0:
                    del cs[left]

        return res

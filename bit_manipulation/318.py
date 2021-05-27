from _ast import List
from collections import defaultdict
from itertools import product


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = defaultdict(int)

        for word in words:
            mask = 0

            for ch in word:
                mask |= (1 << (ord(ch) - ord('a')))

            d[mask] = max(d[mask], len(word))

        return max([d[x] * d[y] for x, y in product(d, d) if x & y == 0] or [0])

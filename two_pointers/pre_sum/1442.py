from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        pre_xor = defaultdict(list)
        pre_xor[0].append(-1)
        xor = 0
        res = 0

        for i, v in enumerate(arr):
            xor ^= v
            pre_xor[xor].append(i)

        for idx_list in pre_xor.values():
            for a, b in product(idx_list, idx_list):
                if a >= b:
                    continue

                res += (b - a - 1)

        return res

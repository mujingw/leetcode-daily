from itertools import accumulate
from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        presum = [0] * length

        for s, e, inc in updates:
            presum[s] += inc

            if e < length - 1:
                presum[e + 1] -= inc

        return list(accumulate(presum))

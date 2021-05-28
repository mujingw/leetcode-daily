from itertools import groupby
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def get_max_len(segment):
            even_neg = 1
            N, first, last = len(segment), -1, -1

            for i, num in enumerate(segment):
                if num < 0:
                    even_neg ^= 1
                    first = i if first == -1 else first
                    last = i

            return N if even_neg else max(N - first - 1, last)

        segments = [list(g) for k, g in groupby(nums, key=lambda x: x != 0) if k != 0]

        return max([get_max_len(segment) for segment in segments] if segments else [0])

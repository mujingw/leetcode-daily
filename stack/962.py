from collections import defaultdict
from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        res = 0
        num_to_idx = defaultdict(list)
        sorted_arr = sorted(A)
        min_idx_so_far = float("inf")

        for i, v in enumerate(A):
            num_to_idx[v].append(i)

        for i in range(len(A) - 1):
            min_idx_so_far = min(min_idx_so_far, num_to_idx[sorted_arr[i]][0])
            res = max(res, num_to_idx[sorted_arr[i + 1]][-1] - min_idx_so_far)

        return res

from typing import List


class Solution:
    """
        0, 1, 2, 3, 4, 5
    [-inf, 3, 1, 2, 4, -inf]

    when i == 5:

    stack of idx    = [0, 2, 3, 4]
    i               = 5
    curr            = 4
    stack[-1]       = 3
    res += 4 * (5 - 4) * (4 - 3)

    i               = 5
    curr            = 3
    stack[-1]       = 2
    res += 3 * (4 - 3) * (3 - 2)

    i               = 5
    curr            = 2
    stack[-1]       = 0
    res += 2 * (5 - 2) * (2 - 0)
    """

    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        idx_non_desc_nums = []
        arr = [float("-inf")] + arr + [float("-inf")]
        res = 0

        for i, val in enumerate(arr):
            while idx_non_desc_nums and arr[idx_non_desc_nums[-1]] > val:
                curr = idx_non_desc_nums.pop()
                num_subarr_r_and_self = i - curr
                num_subarr_l = curr - idx_non_desc_nums[-1]
                # print (f"{i=}, {arr[curr]=}, {num_subarr_l=}, {num_subarr_r_and_self=}")
                res += (arr[curr] * num_subarr_l * num_subarr_r_and_self)

            idx_non_desc_nums.append(i)
            # print (idx_non_desc_nums)

        return res % MOD

from typing import List

from sortedcontainers import SortedDict


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        sd = SortedDict()
        l, r, res = 0, 0, 0

        while r < len(nums):
            new_val = nums[r]
            r += 1

            if new_val not in sd:
                sd[new_val] = 1
            else:
                sd[new_val] += 1

            while abs(sd.keys()[0] - sd.keys()[-1]) > limit:
                rm_val = nums[l]
                l += 1
                sd[rm_val] -= 1

                if sd[rm_val] == 0:
                    del sd[rm_val]

            res = max(res, r - l)

        return res

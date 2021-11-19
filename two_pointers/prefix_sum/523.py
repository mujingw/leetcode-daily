from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum = {0: -1}
        sum_so_far_mod_k = 0

        for i, v in enumerate(nums):
            sum_so_far_mod_k = (sum_so_far_mod_k + v) % k

            if sum_so_far_mod_k in presum:
                if i - presum[sum_so_far_mod_k] >= 2:
                    return True
            else:
                presum[sum_so_far_mod_k] = i

        return False

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg_max, pos_min, prod = float('-inf'), 1, 1
        res = float('-inf')

        for v in nums:
            prod *= v

            if prod > 0:
                res = max(res, prod // pos_min)
                pos_min = min(pos_min, prod)
            elif prod == 0:
                res = max(res, 0)
                neg_max, pos_min, prod = float('-inf'), 1, 1
            else:
                prefix = neg_max if neg_max != float('-inf') else 1
                res = max(res, prod // prefix)
                neg_max = max(neg_max, prod)

        return res

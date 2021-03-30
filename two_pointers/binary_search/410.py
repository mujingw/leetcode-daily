from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def ok(sum_limit, m):
            curr_total = 0
            chunks = 1
            p = 0

            while p < N:
                if nums[p] > sum_limit:
                    return False

                if curr_total + nums[p] <= sum_limit:
                    curr_total += nums[p]
                    p += 1
                else:
                    chunks += 1
                    curr_total = 0

            return chunks <= m

        N = len(nums)
        l, r = 0, sum(nums) + 1

        while l < r:
            mid = (l + r) // 2

            if not ok(mid, m):
                l = mid + 1
            else:
                r = mid

        return l

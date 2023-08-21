from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def ok(max_dist_allowed):
            res, left = 0, 0

            for right, val in enumerate(sn):
                while val - sn[left] > max_dist_allowed:
                    left += 1

                res += (right - left)

            return res >= k

        sn = sorted(nums)
        l, r = 0, sn[-1] - sn[0]

        while l < r:
            mid = (l + r) // 2

            if ok(mid):
                r = mid
            else:
                l = mid + 1

        return l

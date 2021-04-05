from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def ok(dist):
            res, l, r = 0, 0, 0

            while r < N:
                r_val = sn[r]
                r += 1

                while r_val - sn[l] > dist:
                    l += 1

                res += (r - l - 1)

            return res >= k

        sn = sorted(nums)
        N = len(nums)
        l = 0
        r = sn[-1] - sn[0]

        while l < r:
            mid = (l + r) // 2

            if ok(mid):
                r = mid
            else:
                l = mid + 1

        return l

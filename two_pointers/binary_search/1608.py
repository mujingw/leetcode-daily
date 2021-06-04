from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        def ok(x):
            return sum([1 for num in nums if num >= x]) > x

        nums.sort()
        N = len(nums)
        l, r = 1, N

        while l < r:
            mid = (l + r) // 2

            if ok(mid):
                l = mid + 1
            else:
                r = mid

        count = sum([1 for num in nums if num >= l])

        return count if count == l else -1

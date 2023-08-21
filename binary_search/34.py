from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums, t):
            left, right = 0, N - 1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] >= t:
                    right = mid
                else:
                    left = mid + 1

            return left if nums[left] == t else -1

        def find_right(nums, t):
            left, right = 0, N - 1

            while left < right:
                mid = (left + right) // 2

                if nums[mid] <= t:
                    left = mid + 1
                else:
                    right = mid

            return left if nums[left] == t else left - 1

        if not nums:
            return [-1, -1]

        N = len(nums)
        l = find_left(nums, target)

        if l == -1:
            return [-1, -1]

        r = find_right(nums, target)

        return [l, r]

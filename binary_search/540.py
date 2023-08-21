from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    l = mid + 1
                else:
                    r = mid
            else:
                if mid % 2 == 0:
                    r = mid
                else:
                    l = mid + 1

        return nums[l]

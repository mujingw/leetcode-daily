from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] == nums[r]:
                r -= 1
            else:
                if nums[mid] < nums[r]:
                    if nums[mid] < target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid
                else:
                    if nums[l] <= target <= nums[mid]:
                        r = mid
                    else:
                        l = mid + 1

        return nums[l] == target

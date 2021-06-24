from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.kth_smallest(nums, len(nums) - k)

    def kth_smallest(self, nums, k):
        p = self.partition(nums, 0, len(nums) - 1)

        if p == k:
            return nums[p]
        elif p < k:
            return self.kth_smallest(nums[p + 1:], k - p - 1)
        else:
            return self.kth_smallest(nums[:p], k)

    def partition(self, nums, low, high):
        pivot = nums[low]
        le_wall = low

        for i in range(low + 1, high + 1):
            if nums[i] <= pivot:
                le_wall += 1
                nums[i], nums[le_wall] = nums[le_wall], nums[i]

        nums[low], nums[le_wall] = nums[le_wall], nums[low]

        return le_wall

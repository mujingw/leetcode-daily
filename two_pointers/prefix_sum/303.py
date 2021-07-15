from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.presum = {-1: 0}
        sum_so_far = 0

        for i, num in enumerate(nums):
            sum_so_far += num
            self.presum[i] = sum_so_far

    def sumRange(self, i: int, j: int) -> int:
        return self.presum[j] - self.presum[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i, j)

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.N = len(nums) + 1
        self.nums = nums
        self.tree = [0] * self.N

        for i, v in enumerate(nums):
            self._add(i, v)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.nums[index] = val
        self._add(index, delta)

    def _add(self, index, delta):
        index += 1

        while index < self.N:
            self.tree[index] += delta
            index += index & -index

    def _sum(self, index):
        index += 1
        res = 0

        while index > 0:
            res += self.tree[index]
            index -= index & -index

        return res

    def sumRange(self, left: int, right: int) -> int:
        return self._sum(right) - self._sum(left - 1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
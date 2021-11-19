from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.k_sum(res, [], sorted(nums), 0, len(nums) - 1, target, 4)

        return res

    def k_sum(self, res, curr, nums, l, r, t, k):
        if r - l + 1 < k:
            return

        if nums[l] * k > t or nums[r] * k < t:
            return

        if k == 2:
            while l < r:
                s = nums[l] + nums[r]

                if s == t:
                    res.append(curr + [nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < t:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(l, r + 1):
                if i > l and nums[i] == nums[i - 1]:
                    continue

                curr.append(nums[i])
                self.k_sum(res, curr, nums, i + 1, r, t - nums[i], k - 1)
                curr.pop()

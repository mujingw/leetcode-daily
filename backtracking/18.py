from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(res, curr, l, r, t, k):
            if l + k - 1 > r:
                return

            if k < 2:
                return

            if t < nums[l] * k or t > nums[r] * k:
                return

            if k == 2:
                while l < r:
                    s = nums[l] + nums[r]

                    if s == t:
                        res.append(curr + [nums[l], nums[r]])
                        l += 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < t:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r + 1):
                    if i > l and nums[i] == nums[i - 1]:
                        continue

                    curr.append(nums[i])
                    dfs(res, curr, i + 1, r, t - nums[i], k - 1)
                    curr.pop()

        res = []
        nums.sort()
        dfs(res, [], 0, len(nums) - 1, target, 4)

        return res

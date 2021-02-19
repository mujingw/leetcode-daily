class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(res, curr, nums, used):
            if len(curr) == len(nums):
                res.append(curr[:])

                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and not used[i - 1] and nums[i] == nums[i - 1]:
                    continue

                curr.append(nums[i])
                used[i] = True
                dfs(res, curr, nums, used)
                used[i] = False
                curr.pop()

        res = []
        used = [False] * len(nums)
        dfs(res, [], sorted(nums), used)

        return res

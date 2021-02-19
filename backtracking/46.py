class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(res, curr, nums, used):
            if len(curr) == len(nums):
                res.append(curr[:])

                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                curr.append(nums[i])
                used[i] = True
                dfs(res, curr, nums, used)
                used[i] = False
                curr.pop()

        used = [False] * len(nums)
        res = []
        dfs(res, [], nums, used)

        return res

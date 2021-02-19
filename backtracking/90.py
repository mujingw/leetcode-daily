class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(res, curr, nums, start):
            res.append(curr[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                curr.append(nums[i])
                dfs(res, curr, nums, i + 1)
                curr.pop()

        res = []
        dfs(res, [], sorted(nums), 0)

        return res

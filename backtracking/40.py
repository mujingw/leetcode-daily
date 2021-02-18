class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(res, curr, nums, target, start):
            if target < 0:
                return

            if target == 0:
                res.append(curr[:])

                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue

                if nums[i] > target:
                    break

                curr.append(nums[i])
                dfs(res, curr, nums, target - nums[i], i + 1)
                curr.pop()

        res = []
        dfs(res, [], sorted(candidates), target, 0)

        return res

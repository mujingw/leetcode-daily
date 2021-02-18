class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(res, curr, target, nums, start):
            if target < 0:
                return

            if target == 0:
                res.append(curr[:])

                return

            for i in range(start, len(nums)):
                if nums[i] > target:
                    break

                curr.append(nums[i])
                dfs(res, curr, target - nums[i], nums, i)
                curr.pop()

        res = []
        dfs(res, [], target, sorted(candidates), 0)

        return res

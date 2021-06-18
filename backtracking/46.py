from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)

        def dfs(res, curr, nums, used):
            if len(curr) == N:
                res.append(curr[:])
                return

            for i in range(N):
                if used[i]:
                    continue

                curr.append(nums[i])
                used[i] = True
                dfs(res, curr, nums, used)
                used[i] = False
                curr.pop()

        res = []
        dfs(res, [], nums, [False] * N)

        return res

from collections import deque


class Solution(object):
    def maxResult(self, nums, k):
        dp = [float("-inf")] * len(nums)
        dp[0] = nums[0]
        mono_q = deque([0])

        for i, num in enumerate(nums[1:], 1):
            while mono_q and mono_q[0] < i - k:
                mono_q.popleft()

            dp[i] = dp[mono_q[0]] + num

            while mono_q and dp[mono_q[-1]] < dp[i]:
                mono_q.pop()

            mono_q.append(i)

        return dp[-1]

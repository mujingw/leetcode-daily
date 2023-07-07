from collections import deque


class MonoQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        while self.q and self.q[-1] < x:
            self.q.pop()

        self.q.append(x)

    def pop(self, x):
        if self.q and x == self.q[0]:
            self.q.popleft()

    def mx(self):
        return self.q[0]


class Solution(object):
    def maxResult(self, nums, k):
        mono_q = MonoQueue()
        N = len(nums)
        dp = [0] * N
        dp[0] = nums[0]
        mono_q.push(dp[0])

        for i, v in enumerate(nums[1:], 1):
            if i - k - 1 >= 0:
                mono_q.pop(dp[i - k - 1])

            dp[i] = mono_q.mx() + v
            mono_q.push(dp[i])

        return dp[-1]

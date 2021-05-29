from collections import deque
from typing import List


class MonoQueue:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        while self.q and self.q[-1] < x:
            self.q.pop()

        self.q.append(x)

    def pop(self, x):
        if x == self.q[0]:
            self.q.popleft()

    def mx(self):
        return self.q[0]


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [nums[0]]
        window = MonoQueue()
        window.push(nums[0])

        for i, num in enumerate(nums[1:], 1):
            if i > k:
                window.pop(dp[i - k - 1])

            temp = max(num, window.mx() + num)
            dp.append(temp)
            window.push(temp)

        return max(dp)

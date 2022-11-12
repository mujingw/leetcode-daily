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
        return self.q[0] if self.q else 0


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = []
        window = MonoQueue()

        for i, v in enumerate(nums):
            if i > k:
                window.pop(dp[i - k - 1])

            new_max = max(window.mx() + v, v)
            dp.append(new_max)
            window.push(new_max)

        return max(dp)

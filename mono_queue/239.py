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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonoQueue()
        res = []

        for i, num in enumerate(nums):
            if i < k - 1:
                window.push(num)
            else:
                window.push(num)
                res.append(window.mx())
                window.pop(nums[i - k + 1])

        return res

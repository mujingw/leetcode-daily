from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = deque(), []

        for i, v in enumerate(nums):
            while q and nums[q[-1]] < v:
                q.pop()

            q.append(i)

            if i - q[0] >= k:
                q.popleft()

            if i >= k - 1:
                res.append(nums[q[0]])

        return res

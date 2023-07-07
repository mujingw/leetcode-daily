from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = deque([0])
        dp = [0] * len(nums)

        for i, v in enumerate(nums):
            while q and i - q[0] > k:
                q.popleft()

            if q:
                dp[i] = v + dp[q[0]]

            while q and dp[q[-1]] < dp[i]:
                q.pop()

            q.append(i)

        return dp[-1]

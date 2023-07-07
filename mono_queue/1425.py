from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        dp = [0 for _ in range(N)]
        q = deque()

        for i, v in enumerate(nums):
            if q and i - q[0] > k:
                q.popleft()

            dp[i] = max(v, v + (dp[q[0]] if q else 0))

            while q and dp[q[-1]] < dp[i]:
                q.pop()

            q.append(i)

        return max(dp)

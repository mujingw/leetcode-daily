from collections import deque
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        presum = {-1: 0}
        total = 0
        q = deque([-1])
        res = float('inf')

        for i, v in enumerate(nums):
            total += v
            presum[i] = total

            while q and presum[i] - presum[q[0]] >= k:
                res = min(res, i - q[0])
                q.popleft()

            while q and presum[q[-1]] >= presum[i]:
                q.pop()

            q.append(i)

        return res if res != float('inf') else -1

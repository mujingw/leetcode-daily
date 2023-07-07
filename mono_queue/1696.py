from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q = deque([0])
        res = [0] * len(nums)

        for i, v in enumerate(nums):
            while q and i - q[0] > k:
                q.popleft()

            if q:
                res[i] = v + res[q[0]]

            while q and res[q[-1]] < res[i]:
                q.pop()

            q.append(i)

        return res[-1]

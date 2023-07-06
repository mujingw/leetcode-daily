from collections import deque
from typing import List


class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        nums = [y - x for x, y in points]
        q = deque()
        res = float('-inf')

        for i, v in enumerate(nums):
            xj, yj = points[i]

            while q and xj - points[q[0]][0] > k:
                q.popleft()

            if q:
                res = max(res, nums[q[0]] + (xj + yj))

            while q and nums[q[-1]] <= yj - xj:
                q.pop()

            q.append(i)

        return res

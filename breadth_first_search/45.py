from collections import deque
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque([(0, 0)])
        seen = set([0])
        N = len(nums)

        while q:
            curr, dist = q.popleft()

            if curr == N - 1:
                return dist

            for neig in range(curr - nums[curr], curr + nums[curr] + 1):
                if 0 <= neig < N and neig not in seen:
                    seen.add(neig)
                    q.append((neig, dist + 1))

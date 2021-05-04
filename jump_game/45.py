from collections import deque
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        q = deque([(0, 0)])
        seen = {0}
        N = len(nums)

        while q:
            curr, dist = q.popleft()

            if curr == N - 1:
                return dist

            for next_pos in range(curr - nums[curr], curr + nums[curr] + 1):
                if 0 <= next_pos < N and next_pos not in seen:
                    q.append((next_pos, dist + 1))
                    seen.add(next_pos)

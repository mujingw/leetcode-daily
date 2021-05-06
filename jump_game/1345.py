from collections import deque, defaultdict
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = deque([(0, 0)])
        seen = {0}
        val2pos = defaultdict(list)
        N = len(arr)

        for i, num in enumerate(arr):
            val2pos[num].append(i)

        while q:
            curr, dist = q.popleft()

            if curr == N - 1:
                return dist

            next_pos = val2pos[arr[curr]] + [curr + 1, curr - 1]

            for nx in next_pos:
                if 0 <= nx < N and nx not in seen:
                    seen.add(nx)
                    q.append((nx, dist + 1))

            val2pos[arr[curr]] = []

from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        seen = set([start])
        N = len(arr)

        while q:
            curr = q.popleft()

            if arr[curr] == 0:
                return True

            next_pos = curr + arr[curr]

            if next_pos not in seen and 0 <= next_pos < N:
                seen.add(next_pos)
                q.append(next_pos)

            next_pos = curr - arr[curr]

            if next_pos not in seen and 0 <= next_pos < N:
                seen.add(next_pos)
                q.append(next_pos)

        return False

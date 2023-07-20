from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        seen = {start}
        N = len(arr)

        while q:
            curr = q.popleft()

            if arr[curr] == 0:
                return True

            for delta in (arr[curr], -arr[curr]):
                if 0 <= curr + delta < N and curr + delta not in seen:
                    q.append(curr + delta)
                    seen.add(curr + delta)

        return False

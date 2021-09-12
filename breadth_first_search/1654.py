from collections import deque
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        q = deque([(0, "none", 0)])
        seen = set([0])
        forbidden = set(forbidden)
        max_pos = max(x, max(forbidden)) + a + b

        while q:
            curr, incoming_dir, jumps = q.popleft()

            if curr == x:
                return jumps

            if curr + a not in seen and curr + a not in forbidden and curr + a <= max_pos:
                q.append((curr + a, "forward", jumps + 1))
                seen.add(curr + a)

            if incoming_dir != "backward":
                if curr - b >= 0 and curr - b not in forbidden:
                    q.append((curr - b, "backward", jumps + 1))

        return -1

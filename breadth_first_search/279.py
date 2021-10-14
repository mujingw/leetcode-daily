from collections import deque
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        q = deque([(n, 0)])
        seen = {n}

        while q:
            curr, dist = q.popleft()

            if curr == 0:
                return dist

            for i in range(int(sqrt(curr)) + 1):
                next_val = curr - i * i

                if next_val not in seen:
                    seen.add(next_val)
                    q.append((next_val, dist + 1))

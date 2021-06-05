from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deds = set(deadends)

        if "0000" in deds:
            return -1

        q = deque([("0000", 0)])
        seen = {"0000"}

        while q:
            curr, dist = q.popleft()

            if curr == target:
                return dist

            for i in range(len(curr)):
                next_up = curr[:i] + str((int(curr[i]) + 1) % 10) + curr[i + 1:]
                next_down = curr[:i] + str((int(curr[i]) - 1) % 10) + curr[i + 1:]

                for next_step in [next_up, next_down]:
                    if next_step not in seen and next_step not in deds:
                        seen.add(next_step)
                        q.append((next_step, dist + 1))

        return -1

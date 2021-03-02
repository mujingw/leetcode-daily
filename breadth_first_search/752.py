import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        forbidden = set(deadends)

        if "0000" in forbidden:
            return -1

        q = collections.deque([("0000", 0)])
        seen = set(["0000"])

        while q:
            curr, dist = q.popleft()

            if curr == target:
                return dist

            for pos in range(len(curr)):
                nx_up = curr[:pos] + str((int(curr[pos]) + 1) % 10) + curr[pos + 1:]
                nx_down = curr[:pos] + str((int(curr[pos]) - 1) % 10) + curr[pos + 1:]

                if nx_up not in seen and nx_up not in forbidden:
                    q.append((nx_up, dist + 1))
                    seen.add(nx_up)

                if nx_down not in seen and nx_down not in forbidden:
                    q.append((nx_down, dist + 1))
                    seen.add(nx_down)

        return -1

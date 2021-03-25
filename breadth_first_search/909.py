import collections
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        q = collections.deque([(N - 1, 0, 0)])
        seen = set([(N - 1, 0)])
        n2xy = {}
        xy2n = {}
        curr = 1

        for r in range(N - 1, -1, -1):
            cols = [c for c in range(N)]

            if (N - r) % 2 == 0:
                cols = cols[::-1]

            for c in cols:
                n2xy[curr] = (r, c)
                xy2n[(r, c)] = curr
                curr += 1

        while q:
            cx, cy, dist = q.popleft()
            curr_val = xy2n[(cx, cy)]

            if curr_val == N * N:
                return dist

            for i in range(1, 7):
                if 0 < curr_val + i <= N * N:
                    nx, ny = n2xy[curr_val + i]

                    if board[nx][ny] == -1:
                        if (nx, ny) not in seen:
                            seen.add((nx, ny))
                            q.append((nx, ny, dist + 1))
                    else:
                        nx, ny = n2xy[board[nx][ny]]

                        if (nx, ny) not in seen:
                            seen.add((nx, ny))
                            q.append((nx, ny, dist + 1))

        return -1

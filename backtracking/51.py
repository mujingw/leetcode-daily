from collections import defaultdict
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_place_q(x, y):
            if cols[y] or rows[x] or diag[(1, x + y)] or diag[(0, x - y)]:
                return False

            return True

        def add_queen(board, x, y):
            board[x][y] = "Q"
            cols[y] = True
            rows[x] = True
            diag[(0, x - y)] = True
            diag[(1, x + y)] = True

        def remove_queen(board, x, y):
            diag[(0, x - y)] = False
            diag[(1, x + y)] = False
            cols[y] = False
            rows[x] = False
            board[x][y] = "."

        def solve(pos, board, q):
            if pos == EOB:
                if q == N:
                    configs.append([row[:] for row in board])

                return

            x, y = pos // N, pos % N

            if board[x][y] == "." and can_place_q(x, y):
                add_queen(board, x, y)
                solve(pos + 1, board, q + 1)
                remove_queen(board, x, y)

            solve(pos + 1, board, q)

        EOB, N = n * n, n
        board = [["." for _ in range(N)] for _ in range(N)]
        configs = []
        cols = [False] * N
        rows = [False] * N
        diag = defaultdict(bool)
        solve(0, board, 0)

        return [["".join(row) for row in config] for config in configs]

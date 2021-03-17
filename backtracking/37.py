from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(num, x, y):
            for r in range(N):
                if board[r][y] == num and r != x:
                    return False

            for c in range(N):
                if board[x][c] == num and c != y:
                    return False

            base_x, base_y = x // S * S, y // S * S

            for r in range(base_x, base_x + S):
                for c in range(base_y, base_y + S):
                    if board[r][c] == num and (r != x or c != y):
                        return False

            return True

        def solve(pos):
            if pos == EOB:
                return True

            x, y = pos // N, pos % N

            if board[x][y] == ".":
                for num in "123456789":
                    if valid(num, x, y):
                        board[x][y] = num

                        if solve(pos + 1):
                            return True

                        board[x][y] = "."

                return False
            else:
                return solve(pos + 1)

        N, S, EOB = 9, 3, 81
        solve(0)

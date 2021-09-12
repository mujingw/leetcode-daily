from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def bfs(board, i, j, from_val, to_val):
            q = deque([(i, j)])
            seen = {(i, j)}

            while q:
                cx, cy = q.popleft()
                board[cx][cy] = to_val

                for dx, dy in DIR:
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == from_val and (nx, ny) not in seen:
                        seen.add((nx, ny))
                        q.append((nx, ny))

        R, C = len(board), len(board[0])
        DIR = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for i in range(R):
            for j in range(C):
                if i == 0 or i == R - 1 or j == 0 or j == C - 1:
                    if board[i][j] == 'O':
                        bfs(board, i, j, 'O', 'H')

        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'H':
                    board[i][j] = 'O'

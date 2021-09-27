from itertools import product
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(r, c, pos):
            if pos == N:
                return True

            if not (0 <= r < R and 0 <= c < C):
                return False

            if board[r][c] != word[pos]:
                return False

            if (r, c) in visited:
                return False

            visited.add((r, c))
            ok = any(backtrack(r + dx, c + dy, pos + 1) for dx, dy in DIR)
            visited.remove((r, c))

            return ok

        R, C = len(board), len(board[0])
        DIR = ((0, 1), (0, -1), (-1, 0), (1, 0))
        N = len(word)
        visited = set()

        return any(backtrack(r, c, 0) for r, c in product(range(R), range(C)))

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = []

        for r, row in enumerate(board):
            for c, ch in enumerate(row):
                if ch != '.':
                    seen.append((ch, c))
                    seen.append((r, ch))
                    seen.append((r // 3, c // 3, ch))

        return len(seen) == len(set(seen))

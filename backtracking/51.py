from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(queens, xy_sum, xy_diff):
            curr_row = len(queens)

            if curr_row == n:
                res.append(queens[:])

                return

            for curr_col in range(n):
                curr_diff = curr_row - curr_col
                curr_sum = curr_row + curr_col

                if curr_col not in queens and \
                        curr_diff not in xy_diff and \
                        curr_sum not in xy_sum:
                    queens.append(curr_col)
                    xy_diff.append(curr_diff)
                    xy_sum.append(curr_sum)
                    solve(queens, xy_sum, xy_diff)
                    xy_sum.pop()
                    xy_diff.pop()
                    queens.pop()

        res = []
        solve([], [], [])

        return [['.' * q + 'Q' + '.' * (n - q - 1) for q in config] for config in res]

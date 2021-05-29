from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(queens, xy_sum, xy_diff):
            curr_row = len(queens)

            if curr_row == n:
                res.append(queens[:])
                return

            for curr_col in range(n):
                if curr_col in queens:
                    continue

                curr_xy_sum = curr_row + curr_col
                curr_xy_diff = curr_row - curr_col

                if curr_xy_sum not in xy_sum and curr_xy_diff not in xy_diff:
                    queens.append(curr_col)
                    xy_diff.add(curr_xy_diff)
                    xy_sum.add(curr_xy_sum)
                    solve(queens, xy_sum, xy_diff)
                    xy_sum.remove(curr_xy_sum)
                    xy_diff.remove(curr_xy_diff)
                    queens.pop()

        res = []
        solve([], set(), set())

        return [['.' * col + 'Q' + '.' * (n - col - 1) for col in config] for config in res]

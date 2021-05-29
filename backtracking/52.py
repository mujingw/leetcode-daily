class Solution:
    def totalNQueens(self, n: int) -> int:
        def solve(queens, xy_sum, xy_diff):
            curr_row = len(queens)

            if curr_row == n:
                res[0] += 1
                return

            for curr_col in range(n):
                if curr_col in queens:
                    continue

                curr_xy_sum, curr_xy_diff = curr_row + curr_col, curr_row - curr_col

                if curr_xy_sum not in xy_sum and curr_xy_diff not in xy_diff:
                    xy_sum.append(curr_xy_sum)
                    xy_diff.append(curr_xy_diff)
                    queens.append(curr_col)
                    solve(queens, xy_sum, xy_diff)
                    queens.pop()
                    xy_diff.pop()
                    xy_sum.pop()

        res = [0]
        solve([], [], [])

        return res[0]

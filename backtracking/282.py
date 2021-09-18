from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(res, curr, val, pos, prod):
            if pos == N:
                if val == target:
                    res.append(''.join(curr))

                return

            for i in range(pos, N):
                if i != pos and num[pos] == '0':
                    break

                s, v = str(num[pos:i + 1]), int(num[pos:i + 1])

                if not curr:
                    dfs(res, curr + [s], v, i + 1, v)
                else:
                    dfs(res, curr + ['+', s], val + v, i + 1, v)
                    dfs(res, curr + ['-', s], val - v, i + 1, -v)
                    dfs(res, curr + ['*', s], val - prod + prod * v, i + 1, prod * v)

        N = len(num)
        res = []
        dfs(res, [], 0, 0, 0)

        return res

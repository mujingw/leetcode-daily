from itertools import product
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(curr, r, c):
            if not (0 <= r < R and 0 <= c < C):
                return curr

            if grid[r][c] == 0:
                return curr

            if (r, c) in visited:
                return curr

            visited.add((r, c))

            for dx, dy, di in DIR:
                nr, nc = r + dx, c + dy
                curr += (dfs(di, nr, nc) + opposite[di])

            return curr

        R, C = len(grid), len(grid[0])
        DIR = ((0, 1, 'R'), (0, -1, 'L'), (-1, 0, 'U'), (1, 0, 'D'))
        opposite = {'R': 'L', 'D': 'U', 'U': 'D', 'L': 'R'}
        visited = set()
        islands = set()

        for r, c in product(range(R), range(C)):
            if grid[r][c] == 1:
                signature = dfs('S', r, c)

                if signature != 'S':
                    islands.add(signature)

        return len(islands)

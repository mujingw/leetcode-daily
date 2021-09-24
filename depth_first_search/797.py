from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(res, path, node):
            if node == N - 1:
                res.append(path[:])

                return

            for neig in graph[node]:
                path.append(neig)
                dfs(res, path, neig)
                path.pop()

        N = len(graph)
        res = []
        dfs(res, [0], 0)

        return res

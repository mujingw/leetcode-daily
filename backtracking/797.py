from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.target = len(graph) - 1
        self.backtrack(res, [0], 0, graph)

        return res

    def backtrack(self, res, curr, node, graph):
        if node == self.target:
            res.append(curr[:])

            return

        for ng in graph[node]:
            curr.append(ng)
            self.backtrack(res, curr, ng, graph)
            curr.pop()

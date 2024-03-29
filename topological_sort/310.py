from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]

        g = self.build_graph(edges)
        indegree = [len(g[i]) for i in range(n)]
        leaves = [i for i in range(n) if indegree[i] == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                for ng in g[leaf]:
                    indegree[ng] -= 1

                    if indegree[ng] == 1:
                        new_leaves.append(ng)

            leaves = new_leaves[:]

        return leaves

    def build_graph(self, edges):
        g = defaultdict(list)

        for f, t in edges:
            g[f].append(t)
            g[t].append(f)

        return g

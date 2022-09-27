from collections import deque, defaultdict
from typing import List


class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        res = []
        g = self.build_graph(pre)
        indeg = self.get_indeg(pre)
        q = deque([x for x in range(n) if indeg[x] == 0])

        while q:
            curr = q.popleft()
            res.append(curr)

            for neig in g[curr]:
                indeg[neig] -= 1

                if indeg[neig] == 0:
                    q.append(neig)

        return res if len(res) == n else []

    def build_graph(self, pre):
        g = defaultdict(list)

        for second, first in pre:
            g[first].append(second)

        return g

    def get_indeg(self, pre):
        indeg = defaultdict(int)

        for second, first in pre:
            indeg[second] += 1

        return indeg

import collections
from collections import defaultdict
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def bfs(root):
            q = collections.deque([(root, 0)])
            res = 0

            while q:
                curr, dist = q.popleft()
                res = max(res, dist)

                for direct_report in g[curr]:
                    q.append((direct_report, dist + informTime[curr]))

            return res

        g = defaultdict(set)
        root = None

        for emp, mgr in enumerate(manager):
            if mgr != -1:
                g[mgr].add(emp)
            else:
                root = emp

        return bfs(root)

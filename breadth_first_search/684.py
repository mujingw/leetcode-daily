from collections import defaultdict, deque
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def bfs(src, tgt):
            q = deque([src])
            seen = {src}

            while q:
                curr = q.popleft()

                if curr == tgt:
                    return True

                for neig in g[curr]:
                    if neig not in seen:
                        seen.add(neig)
                        q.append(neig)

            return False

        g = defaultdict(set)
        res = None

        for u, v in edges:
            if not bfs(u, v):
                g[u].add(v)
                g[v].add(u)
            else:
                res = [u, v]

        return res

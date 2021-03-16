import collections
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def bfs(node):
            q = collections.deque([(node, 'B')])
            blue.add(node)

            while q:
                curr, color = q.popleft()

                for neig in graph[curr]:
                    if neig not in blue and neig not in red:
                        if color == 'B':
                            red.add(neig)
                            q.append((neig, 'R'))
                        else:
                            blue.add(neig)
                            q.append((neig, 'B'))

        blue, red = set([]), set([])
        N = len(graph)

        for i in range(N):
            if i not in blue and i not in red:
                bfs(i)

        for i in range(N):
            for node in graph[i]:
                if i in blue and node in blue:
                    return False

                if i in red and node in red:
                    return False

        return True

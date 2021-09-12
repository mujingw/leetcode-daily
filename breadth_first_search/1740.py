from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def build_graph_find_src(root, p):
            q = deque([root])
            g = defaultdict(set)
            src = None

            while q:
                curr = q.popleft()

                if curr.val == p:
                    src = curr

                if curr.left:
                    g[curr].add(curr.left)
                    g[curr.left].add(curr)
                    q.append(curr.left)

                if curr.right:
                    g[curr].add(curr.right)
                    g[curr.right].add(curr)
                    q.append(curr.right)

            return g, src

        def bfs(g, src, target):
            q = deque([(src, 0)])
            seen = set([src])

            while q:
                curr, dist = q.popleft()

                if curr.val == target:
                    return dist

                for neig in g[curr]:
                    if neig not in seen:
                        seen.add(neig)
                        q.append((neig, dist + 1))

        if p == q:
            return 0

        g, src = build_graph_find_src(root, p)

        return bfs(g, src, q)

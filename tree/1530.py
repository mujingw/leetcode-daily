import collections
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def bfs(src):
            q = collections.deque([(src, 0)])
            seen = set([src])

            while q:
                curr, dist = q.popleft()

                if curr in leaves and curr is not src:
                    res[0] += 1

                for neig in g[curr]:
                    if neig not in seen and dist + 1 <= distance:
                        seen.add(neig)
                        q.append((neig, dist + 1))

        def dfs(leaves, root):
            if not root:
                return

            if not root.left and not root.right:
                leaves.add(root)
            else:
                if root.left:
                    g[root].add(root.left)
                    g[root.left].add(root)

                if root.right:
                    g[root].add(root.right)
                    g[root.right].add(root)

                dfs(leaves, root.left)
                dfs(leaves, root.right)

        g = defaultdict(set)
        leaves = set()
        dfs(leaves, root)
        res = [0]

        for leaf in leaves:
            bfs(leaf)

        return res[0] // 2

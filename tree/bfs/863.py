from collections import defaultdict, deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        g = defaultdict(set)

        def dfs(node):
            if not node:
                return

            if node.left:
                g[node].add(node.left)
                g[node.left].add(node)
                dfs(node.left)

            if node.right:
                g[node].add(node.right)
                g[node.right].add(node)
                dfs(node.right)

        dfs(root)
        q = deque([(target, 0)])
        seen = {target}
        res = []

        while q:
            curr, dist = q.popleft()

            if dist > K:
                break

            if dist == K:
                res.append(curr.val)

            for neighbor in g[curr]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    q.append((neighbor, dist + 1))

        return res

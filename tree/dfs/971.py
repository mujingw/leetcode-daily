from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(root):
            if not root or not q:
                return

            if root.val != q[0]:
                res.append(None)
                return

            q.popleft()

            if root.left and root.left.val != q[0]:
                res.append(root.val)
                dfs(root.right)
                dfs(root.left)
            else:
                dfs(root.left)
                dfs(root.right)

        N, q, res = len(voyage), deque(voyage), []
        dfs(root)

        return res if None not in res else [-1]

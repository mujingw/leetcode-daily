from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[2]

    def dfs(self, node):
        if not node:
            return float('inf'), float('-inf'), True

        lmin, lmax, lok = self.dfs(node.left)
        rmin, rmax, rok = self.dfs(node.right)

        if lmax < node.val < rmin:
            return min(lmin, node.val), max(rmax, node.val), lok and rok
        else:
            return float('-inf'), float('inf'), False

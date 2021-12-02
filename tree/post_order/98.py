from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.postorder(root)[2]

    def postorder(self, node):
        if not node:
            return float('inf'), float('-inf'), True

        lmin, lmax, lok = self.postorder(node.left)
        rmin, rmax, rok = self.postorder(node.right)

        if lmax < node.val < rmin:
            return min(lmin, node.val), max(node.val, rmax), lok and rok
        else:
            return float('-inf'), float('inf'), False

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        self.postorder(root)

        return self.res

    def postorder(self, node):
        if not node:
            return 0

        lsum = self.postorder(node.left)
        rsum = self.postorder(node.right)
        self.res = max(self.res, max(0, lsum) + max(0, rsum) + node.val)

        return max(0, lsum, rsum) + node.val

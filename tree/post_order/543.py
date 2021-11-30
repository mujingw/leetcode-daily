from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        self.dfs(root)

        return self.longest

    def dfs(self, node):
        if not node:
            return 0

        ld, rd = self.dfs(node.left), self.dfs(node.right)
        self.longest = max(self.longest, ld + rd)

        return max(ld, rd) + 1

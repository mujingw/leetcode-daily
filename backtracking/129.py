from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.backtrack(0, root)

        return self.res

    def backtrack(self, curr, node):
        if not node:
            return

        if not node.left and not node.right:
            self.res += curr * 10 + node.val
        else:
            self.backtrack(curr * 10 + node.val, node.left)
            self.backtrack(curr * 10 + node.val, node.right)

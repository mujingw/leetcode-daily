from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, False, {})

    def dfs(self, node, parent_robbed, memo):
        if not node:
            return 0

        if (node, parent_robbed) in memo:
            return memo[(node, parent_robbed)]

        if parent_robbed:
            res = self.dfs(node.left, False, memo) + self.dfs(node.right, False, memo)
        else:
            res = max(node.val + self.dfs(node.left, True, memo) + self.dfs(node.right, True, memo),
                      self.dfs(node.left, False, memo) + self.dfs(node.right, False, memo))

        memo[(node, parent_robbed)] = res

        return res

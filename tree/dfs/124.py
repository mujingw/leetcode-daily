# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(res, node):
            if not node:
                return float('-inf')

            left = dfs(res, node.left)
            right = dfs(res, node.right)
            local_sum = left + right + node.val
            res[0] = max(res[0], local_sum, left + node.val, right + node.val, node.val)

            return max(left + node.val, right + node.val, node.val)

        res = [float('-inf')]
        dfs(res, root)

        return res[0]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(res, root):
            if not root:
                return 0

            l_depth, r_depth = dfs(res, root.left), dfs(res, root.right)

            if root.left and root.left.val == root.val:
                l_depth += 1
            else:
                l_depth = 0

            if root.right and root.right.val == root.val:
                r_depth += 1
            else:
                r_depth = 0

            res[0] = max(res[0], l_depth + r_depth)

            return max(l_depth, r_depth)

        res = [0]
        dfs(res, root)

        return res[0]

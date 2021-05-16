# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 1

            l, r = dfs(node.left), dfs(node.right)

            if l == 0 or r == 0:
                self.res += 1

                return 2
            elif l == 2 or r == 2:
                return 1
            else:
                return 0

        self.res = 0

        if dfs(root) == 0:
            self.res += 1

        return self.res

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        sums_seen = set()

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            s = left + right + node.val
            sums_seen.add(s)

            return s

        total = root.val + dfs(root.left) + dfs(root.right)

        return total % 2 == 0 and total // 2 in sums_seen

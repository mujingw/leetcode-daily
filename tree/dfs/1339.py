from functools import lru_cache
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def get_sum(node):
            if not node:
                return 0

            return node.val + get_sum(node.left) + get_sum(node.right)

        def traverse(res, node, total):
            if not node:
                return

            left = get_sum(node.left)
            right = get_sum(node.right)
            res[0] = max(res[0], left * (total - left), right * (total - right))

            traverse(res, node.left, total)
            traverse(res, node.right, total)

        MOD = 10 ** 9 + 7
        res = [0]
        traverse(res, root, get_sum(root))

        return res[0] % MOD

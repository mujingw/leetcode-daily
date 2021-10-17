from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        self.res = 0
        d = defaultdict(int)
        d[0] += 1
        self.dfs(0, d, root, target_sum)

        return self.res

    def dfs(self, total, d, node, target):
        if not node:
            return

        total += node.val
        need = total - target
        self.res += d[need]
        d[total] += 1
        self.dfs(total, d, node.left, target)
        self.dfs(total, d, node.right, target)
        d[total] -= 1

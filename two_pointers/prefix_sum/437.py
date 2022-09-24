from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        res = [0]
        presum = defaultdict(int)
        presum[0] = 1
        self.backtrack(res, root, 0, presum, target)

        return res[0]

    def backtrack(self, res, node, total, presum, target):
        if not node:
            return

        total += node.val
        res[0] += presum[total - target]
        presum[total] += 1
        self.backtrack(res, node.left, total, presum, target)
        self.backtrack(res, node.right, total, presum, target)
        presum[total] -= 1

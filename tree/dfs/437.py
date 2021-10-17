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
        self.backtrack(0, d, root, target_sum)

        return self.res

    def backtrack(self, sum_so_far, d, node, target):
        if not node:
            return

        sum_so_far += node.val
        diff_needed = sum_so_far - target
        self.res += d[diff_needed]
        d[sum_so_far] += 1
        self.backtrack(sum_so_far, d, node.left, target)
        self.backtrack(sum_so_far, d, node.right, target)
        d[sum_so_far] -= 1

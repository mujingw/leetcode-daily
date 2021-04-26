from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> int:
        def dfs(res, node, curr, d, t):
            if not node:
                return

            if d[(curr + node.val) - t] > 0:
                res[0] += d[curr + node.val - t]

            d[curr + node.val] += 1
            dfs(res, node.left, curr + node.val, d, t)
            dfs(res, node.right, curr + node.val, d, t)
            d[curr + node.val] -= 1

        res = [0]
        d = defaultdict(int)
        d[0] = 1
        dfs(res, root, 0, d, target_sum)

        return res[0]

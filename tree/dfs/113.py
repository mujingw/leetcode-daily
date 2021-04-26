from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, target_sum: int) -> List[List[int]]:
        def dfs(res, curr, node, t):
            if not node:
                return

            curr.append(node.val)

            if node.left is None and node.right is None:
                if node.val == t:
                    res.append(curr[:])
            else:
                dfs(res, curr, node.left, t - node.val)
                dfs(res, curr, node.right, t - node.val)

            curr.pop()

        res = []
        dfs(res, [], root, target_sum)

        return res

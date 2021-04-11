from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res, stack = [], [root, root]

        while stack:
            curr = stack.pop()

            if stack and stack[-1] == curr:
                if curr.right:
                    stack.extend([curr.right, curr.right])

                if curr.left:
                    stack.extend([curr.left, curr.left])
            else:
                res.append(curr.val)

        return res

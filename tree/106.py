from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def construct(inorder, postorder, il, ir, pl, pr):
            if pl == pr:
                return None

            root = TreeNode(postorder[pr - 1])
            idx = inorder[il:ir].index(root.val)
            root.left = construct(inorder, postorder, il, il + idx, pl, pl + idx)
            root.right = construct(inorder, postorder, il + idx + 1, ir, pl + idx, pr - 1)

            return root

        N = len(inorder)

        return construct(inorder, postorder, 0, N, 0, N)

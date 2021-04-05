from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def construct(preorder, inorder, pl, pr, il, ir):
            if pl == pr:
                return None

            root = TreeNode(preorder[pl])
            idx = inorder[il:ir].index(root.val)
            root.left = construct(preorder, inorder, pl + 1, pl + 1 + idx, il, il + idx)
            root.right = construct(preorder, inorder, pl + 1 + idx, pr, il + idx + 1, ir)

            return root

        N = len(preorder)

        return construct(preorder, inorder, 0, N, 0, N)

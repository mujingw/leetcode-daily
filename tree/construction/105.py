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
            idx = lookup[root.val]
            num_left_nodes = idx - il
            root.left = construct(preorder, inorder, pl + 1, pl + 1 + num_left_nodes, il, idx)
            root.right = construct(preorder, inorder, pl + 1 + num_left_nodes, pr, idx + 1, ir)

            return root

        N = len(preorder)
        lookup = {}

        for i, v in enumerate(inorder):
            lookup[v] = i

        return construct(preorder, inorder, 0, N, 0, N)

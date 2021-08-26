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
            idx = lookup[root.val]
            num_left_nodes = idx - il
            root.left = construct(inorder, postorder, il, idx, pl, pl + num_left_nodes)
            root.right = construct(inorder, postorder, idx + 1, ir, pl + num_left_nodes, pr - 1)

            return root

        N = len(inorder)
        lookup = {}

        for i, v in enumerate(inorder):
            lookup[v] = i

        return construct(inorder, postorder, 0, N, 0, N)

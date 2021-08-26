# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        m = {v: i for i, v in enumerate(postorder)}
        N = len(postorder)

        def build(pre, i, j, post, x, y):
            if i >= j or x >= y:
                return None

            root = TreeNode(pre[i])

            if j - i > 1:
                idx = m[pre[i + 1]]
                left_child_size = idx + 1 - x
                root.left = build(pre, i + 1, i + 1 + left_child_size, post, x, x + left_child_size)
                root.right = build(pre, i + 1 + left_child_size, j, post, x + left_child_size, y - 1)

            return root

        return build(preorder, 0, N, postorder, 0, N)

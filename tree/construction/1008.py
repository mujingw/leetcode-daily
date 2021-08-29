from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def build(arr, start, end):
            if start >= end:
                return None

            root = TreeNode(arr[start])
            idx = start + 1

            while idx < end and arr[idx] < arr[start]:
                idx += 1

            root.left = build(arr, start + 1, idx)
            root.right = build(arr, idx, end)

            return root

        return build(preorder, 0, len(preorder))

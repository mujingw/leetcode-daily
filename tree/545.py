from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        self.res = [root.val]
        self.get_left(root.left)
        self.get_leaves(root)
        self.get_right(root.right)

        return self.res

    def get_left(self, node):
        if not node:
            return

        if not node.left and not node.right:
            return

        self.res.append(node.val)

        if node.left:
            self.get_left(node.left)
        else:
            self.get_left(node.right)

    def get_right(self, node):
        if not node:
            return

        if not node.left and not node.right:
            return

        if node.right:
            self.get_right(node.right)
        else:
            self.get_right(node.left)

        self.res.append(node.val)

    def get_leaves(self, node):
        if not node:
            return

        if not node.left and not node.right:
            self.res.append(node.val)

            return

        self.get_leaves(node.left)
        self.get_leaves(node.right)

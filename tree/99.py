from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def push_left(s, root):
            while root:
                s.append(root)
                root = root.left

        def inorder(root):
            res = []
            s = []
            push_left(s, root)

            while s:
                curr = s.pop()
                res.append(curr.val)
                push_left(s, curr.right)

            return res

        vals = deque(sorted(inorder(root)))
        s = []
        push_left(s, root)

        while s:
            curr = s.pop()
            curr.val = vals.popleft()
            push_left(s, curr.right)

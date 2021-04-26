from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        q = deque([root])
        res = 0

        while q:
            curr = q.popleft()
            res += 1

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

        return res

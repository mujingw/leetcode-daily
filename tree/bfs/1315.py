from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        q = deque([(root, False, False)])
        res = 0

        while q:
            size = len(q)

            for _ in range(size):
                curr, is_parent_even, ok = q.popleft()
                res += curr.val if ok else 0

                if curr.left:
                    q.append((curr.left, curr.val % 2 == 0, is_parent_even))

                if curr.right:
                    q.append((curr.right, curr.val % 2 == 0, is_parent_even))

        return res

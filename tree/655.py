from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_max_depth(node):
            if not node:
                return 0

            left = get_max_depth(node.left)
            right = get_max_depth(node.right)

            return max(left, right) + 1

        height = get_max_depth(root)
        width = 2 ** height - 1
        res = [["" for _ in range(width)] for _ in range(height)]
        q = deque([(root, 0, width // 2)])

        while q:
            curr, row, col = q.popleft()
            res[row][col] = str(curr.val)
            offset = 2 ** (height - row - 2)

            if curr.left:
                q.append((curr.left, row + 1, col - offset))

            if curr.right:
                q.append((curr.right, row + 1, col + offset))

        return res

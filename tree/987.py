from collections import defaultdict, deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        y2node = defaultdict(list)
        res = []
        q = deque([(root, 0, 0)])

        while q:
            curr, x, y = q.popleft()
            y2node[y].append((curr.val, x))

            if curr.left:
                q.append((curr.left, x + 1, y - 1))

            if curr.right:
                q.append((curr.right, x + 1, y + 1))

        for y in sorted(y2node.keys()):
            res.append([x[0] for x in sorted(y2node[y], key=lambda x: (x[1], x[0]))])

        return res

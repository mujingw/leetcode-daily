# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def helper(node):
            if not node:
                return float('inf'), float('-inf'), 0

            lmin, lmax, lcount = helper(node.left)
            rmin, rmax, rcount = helper(node.right)

            if lmax < node.val < rmin:
                return min(lmin, node.val), max(node.val, rmax), lcount + rcount + 1
            else:
                return float('-inf'), float('inf'), max(lcount, rcount)

        mi, mx, count = helper(root)

        return count

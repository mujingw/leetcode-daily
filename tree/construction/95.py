from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(nums):
            if not nums:
                return [None]

            res = []

            for i in range(len(nums)):
                left_subtrees = helper(nums[:i])
                right_subtrees = helper(nums[i + 1:])

                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(nums[i])
                        root.left = left
                        root.right = right

                        res.append(root)

            return res

        return helper([i for i in range(1, n + 1)])

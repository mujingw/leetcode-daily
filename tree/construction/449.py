from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def __init__(self):
        self.DELIMITER = ','

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """

        def helper(res, root):
            if not root:
                return

            res.append(str(root.val))
            helper(res, root.left)
            helper(res, root.right)

        res = []
        helper(res, root)

        return self.DELIMITER.join(res)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def helper(q, lower, upper):
            if q and q[0] == '':
                return None

            if not (q and lower <= int(q[0]) <= upper):
                return None

            curr = int(q.popleft())
            root = TreeNode(curr)
            root.left = helper(q, lower, curr)
            root.right = helper(q, curr, upper)

            return root

        return helper(deque(data.split(self.DELIMITER)), float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

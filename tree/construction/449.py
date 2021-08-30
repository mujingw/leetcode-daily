from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def __init__(self):
        self.NULL_NODE = 'X'
        self.DELIMITER = ','

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return self.NULL_NODE

        return self.DELIMITER.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """

        def helper(q):
            curr = q.popleft()

            if curr == self.NULL_NODE:
                return None

            root = TreeNode(curr)
            root.left = helper(q)
            root.right = helper(q)

            return root

        return helper(deque(data.split(self.DELIMITER)))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

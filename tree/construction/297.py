from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def __init__(self):
        self.NULL_NODE = '#'
        self.DELIMITER = ','

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return self.NULL_NODE

        return self.DELIMITER.join([str(root.val),
                                    self.serialize(root.left),
                                    self.serialize(root.right)])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper(nodes):
            curr = nodes.popleft()

            if curr == self.NULL_NODE:
                return None

            root = TreeNode(curr)
            root.left = helper(nodes)
            root.right = helper(nodes)

            return root

        return helper(deque(data.split(self.DELIMITER)))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

# Definition for a Node.
import collections


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Codec:
    def __init__(self):
        self.NODE_DELIMITER = ","
        self.NULL = "X"

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

        def bfs(root):
            q = collections.deque([root, None])
            res = []

            while q:
                size = len(q)

                for i in range(size):
                    curr = q.popleft()

                    if curr:
                        res.append(str(curr.val))

                        for child in curr.children:
                            q.append(child)

                        q.append(None)
                    else:
                        res.append(self.NULL)

            rep = self.NODE_DELIMITER.join(res)

            return rep

        return bfs(root)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

        def build_tree(root, nodes):
            q = collections.deque([root])

            while q:
                curr = q.popleft()
                curr.children = []

                while nodes:
                    child_val = nodes.popleft()

                    if child_val == self.NULL:
                        break
                    else:
                        child = Node(int(child_val))
                        curr.children.append(child)
                        q.append(child)

            return root

        nodes = collections.deque(data.split(self.NODE_DELIMITER))
        root_val = nodes.popleft()

        if root_val == self.NULL:
            return None

        root = Node(int(root_val))
        nodes.popleft()

        return build_tree(root, nodes)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

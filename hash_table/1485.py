# Definition for Node.
class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


# Definition for NodeCopy.
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return root

        d = {root: NodeCopy(root.val)}
        self.dfs(root, d)

        return d[root]

    def dfs(self, node, d):
        if not node:
            return

        if node.left:
            if node.left not in d:
                d[node.left] = NodeCopy(node.left.val)

            d[node].left = d[node.left]

        if node.right:
            if node.right not in d:
                d[node.right] = NodeCopy(node.right.val)

            d[node].right = d[node.right]

        if node.random:
            if node.random not in d:
                d[node.random] = NodeCopy(node.random.val)

            d[node].random = d[node.random]

        self.dfs(node.left, d)
        self.dfs(node.right, d)

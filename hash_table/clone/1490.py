# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root

        d = {root: Node(root.val)}
        self.dfs(root, d)

        return d[root]

    def dfs(self, node, d):
        if not node:
            return

        for child in node.children:
            if child not in d:
                d[child] = Node(child.val)

            d[node].children.append(d[child])
            self.dfs(child, d)

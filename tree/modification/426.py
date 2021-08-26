# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def push_left(node, s):
            while node:
                s.append(node)
                node = node.left

        if not root:
            return None

        dummy = Node(-1)
        curr = dummy
        stack = []
        push_left(root, stack)

        while stack:
            node = stack.pop()
            curr.right = node
            node.left = curr
            curr = curr.right
            push_left(node.right, stack)

        dummy.right.left = curr
        curr.right = dummy.right

        return dummy.right

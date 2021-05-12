# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None

        dummy = Node(-1, None, None, None)
        tail = dummy
        stack = [head]

        while stack:
            curr = stack.pop()
            tail.next = curr
            tail.next.prev = tail
            tail = tail.next

            if curr.next:
                stack.append(curr.next)
                curr.next = None

            if curr.child:
                stack.append(curr.child)
                curr.child = None

        dummy.next.prev = None

        return dummy.next

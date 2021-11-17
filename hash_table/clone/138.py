# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head

        d = {head: Node(head.val)}
        curr = head

        while curr:
            if curr.random:
                if curr.random not in d:
                    d[curr.random] = Node(curr.random.val)

                d[curr].random = d[curr.random]

            if curr.next:
                if curr.next not in d:
                    d[curr.next] = Node(curr.next.val)

                d[curr].next = d[curr.next]

            curr = curr.next

        return d[head]

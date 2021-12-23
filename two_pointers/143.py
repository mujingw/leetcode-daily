from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        l1, l2 = self.split(head)
        l2 = self.reverse(l2)

        return self.merge(l1, l2)

    def split(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = dummy.next
        l2 = slow.next
        slow.next = None

        return l1, l2

    def reverse(self, head):
        dummy = ListNode(-1)
        curr = head

        while curr:
            node = curr
            curr = curr.next
            node.next = dummy.next
            dummy.next = node

        return dummy.next

    def merge(self, l1, l2):
        dummy = ListNode(-1)
        curr = dummy

        while l1 or l2:
            if l1:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
                curr.next = None

            if l2:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
                curr.next = None

        return dummy.next

    def print(self, head):
        res = []
        curr = head

        while curr:
            res.append(str(curr.val))
            curr = curr.next

        print('->'.join(res))

from heapq import heappush, heappop
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        dummy = ListNode(-1)
        curr = dummy

        for i, head in enumerate(lists):
            if head:
                heappush(h, (head.val, i, head))

        while h:
            val, list_idx, node = heappop(h)

            if node.next:
                new_val, new_head = node.next.val, node.next
                heappush(h, (new_val, list_idx, new_head))

            curr.next = node
            curr = curr.next
            curr.next = None

        return dummy.next

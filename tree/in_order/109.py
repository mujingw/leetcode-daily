# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_len(head):
            curr = head
            res = 0

            while curr:
                res += 1
                curr = curr.next

            return res

        def helper(start, end):
            if start > end:
                return None

            mid = (start + end) // 2

            left = helper(start, mid - 1)
            root = TreeNode(self.curr.val)
            self.curr = self.curr.next
            root.left = left
            root.right = helper(mid + 1, end)

            return root

        self.curr = head

        return helper(0, get_len(head) - 1)

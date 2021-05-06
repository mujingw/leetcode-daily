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
        def helper(nodes):
            if not nodes:
                return None

            N = len(nodes)
            root = TreeNode(nodes[N // 2])
            root.left = helper(nodes[:N // 2])
            root.right = helper(nodes[N // 2 + 1:])

            return root

        nodes = []
        curr = head

        while curr:
            nodes.append(curr.val)
            curr = curr.next

        return helper(nodes)

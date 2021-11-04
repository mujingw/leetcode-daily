class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val


class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode(-1)
        self.size = 0

    def get(self, index: int) -> int:
        if index < self.size:
            curr = self.dummy.next

            for i in range(index):
                curr = curr.next

            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if 0 <= index <= self.size:
            curr = self.dummy

            for i in range(index):
                curr = curr.next

            self._add_node(val, curr)

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.size:
            curr = self.dummy

            for i in range(index):
                curr = curr.next

            curr.next = curr.next.next
            self.size -= 1

    def _add_node(self, val, prev):
        new_node = ListNode(val)
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1

        return new_node

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.d = {}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        node = self.d[key]
        self._promote(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            node = Node(key, value)
            self.d[key] = node
            self._front_insert(node)
        else:
            node = self.d[key]
            node.val = value
            self._promote(node)

        if len(self.d) > self.capacity:
            self._evict()

    def _front_insert(self, node):
        old_first = self.head.next
        node.next = old_first
        old_first.prev = node
        node.prev = self.head
        self.head.next = node

    def _promote(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        node.prev = None
        node.next = None
        self._front_insert(node)

    def _evict(self):
        if len(self.d) == 0:
            return

        last = self.tail.prev
        self.tail.prev = last.prev
        last.prev.next = self.tail
        last.prev = None
        last.next = None
        del self.d[last.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)

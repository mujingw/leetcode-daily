from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.k = capacity

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)

            return self[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self[key] = value
        self.move_to_end(key)

        if len(self) > self.k:
            self.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)

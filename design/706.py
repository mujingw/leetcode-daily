class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.CAPACITY = 769
        self.buckets = [None] * self.CAPACITY

    def get_hash(self, key):
        h = hash(key)

        return h ^ (h >> 16)

    def get_loc(self, key):
        return (self.CAPACITY - 1) & self.get_hash(key)

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        loc = self.get_loc(key)

        if not self.buckets[loc]:
            self.buckets[loc] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.buckets[loc]):
                if k == key:
                    self.buckets[loc][i] = (key, value)
                    return

            self.buckets[loc].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        loc = self.get_loc(key)

        if not self.buckets[loc]:
            return -1
        else:
            for k, v in self.buckets[loc]:
                if k == key:
                    return v

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        loc = self.get_loc(key)

        if self.buckets[loc]:
            for i, (k, v) in enumerate(self.buckets[loc]):
                if k == key:
                    self.buckets[loc].pop(i)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key, value)
# param_2 = obj.get(key)
# obj.remove(key)

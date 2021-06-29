from sortedcontainers import SortedList


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.CAPACITY = 100
        self.buckets = [None] * self.CAPACITY

    def get_loc(self, key):
        return (self.CAPACITY - 1) & hash(key)

    def add(self, key: int) -> None:
        loc = self.get_loc(key)

        if not self.buckets[loc]:
            self.buckets[loc] = SortedList([key])
        elif not self.contains(key):
            self.buckets[loc].add(key)

    def remove(self, key: int) -> None:
        loc = self.get_loc(key)

        if self.contains(key):
            self.buckets[loc].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        loc = self.get_loc(key)

        return self.buckets[loc] and key in self.buckets[loc]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

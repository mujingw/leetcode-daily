class Node:
    def __init__(self):
        self.children = {}
        self.val = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word, val):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()

            curr = curr.children[ch]

        curr.val = val

    def get_sum(self, prefix):
        def dfs(res, root):
            res[0] += root.val

            for child in root.children.values():
                dfs(res, child)

        curr = self.root
        res = [0]

        for ch in prefix:
            if ch not in curr.children:
                return 0

            curr = curr.children[ch]

        dfs(res, curr)

        return res[0]


class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.store = Trie()

    def insert(self, key: str, val: int) -> None:
        self.store.add(key, val)

    def sum(self, prefix: str) -> int:
        return self.store.get_sum(prefix)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key, val)
# param_2 = obj.sum(prefix)

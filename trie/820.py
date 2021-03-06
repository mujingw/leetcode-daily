from typing import List


class Node:
    def __init__(self, depth=0):
        self.children = {}
        self.depth = depth


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        curr = self.root

        for i, ch in enumerate(word):
            if ch not in curr.children:
                curr.children[ch] = Node(i + 1)

            curr = curr.children[ch]

    def size(self):
        return self.dfs(self.root)

    def dfs(self, root):
        if not root:
            return 0

        if len(root.children) == 0:
            return root.depth + 1

        count = 0

        for ch in root.children:
            count += self.dfs(root.children[ch])

        return count


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()

        for word in words:
            trie.add(word[::-1])

        return trie.size()

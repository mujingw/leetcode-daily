from typing import List


class Node:
    def __init__(self):
        self.children = {}
        self.indexes = []


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixes = Node()
        self.suffixes = Node()

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]
                self.add_to_trie(prefix, self.prefixes, i)
                self.add_to_trie(suffix, self.suffixes, i)

    def add_to_trie(self, xfix, root, idx):
        curr = root

        for ch in xfix:
            if ch not in curr.children:
                curr.children[ch] = Node()

            curr = curr.children[ch]

        curr.indexes.append(idx)

    def f(self, prefix: str, suffix: str) -> int:
        p_idx = self.search(self.prefixes, prefix)
        s_idx = self.search(self.suffixes, suffix)
        p, q = len(p_idx) - 1, len(s_idx) - 1

        while p >= 0 and q >= 0:
            if p >= 0 and q >= 0 and p_idx[p] == s_idx[q]:
                return p_idx[p]
            elif p >= 0 and q >= 0 and p_idx[p] > s_idx[q]:
                p -= 1
            elif p >= 0 and q >= 0 and p_idx[p] < s_idx[q]:
                q -= 1

        return -1

    def search(self, curr, xfix):
        for ch in xfix:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return []

        return curr.indexes

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix, suffix)

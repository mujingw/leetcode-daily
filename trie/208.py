class Node:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()

            curr = curr.children[ch]

        curr.is_word = True

    def search(self, word: str) -> bool:
        return self._search(word, True)

    def startsWith(self, prefix: str) -> bool:
        return self._search(prefix, False)

    def _search(self, target, is_full_word) -> bool:
        curr = self.root

        for ch in target:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return False

        return curr.is_word if is_full_word else True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

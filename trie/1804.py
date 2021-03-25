class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0
        self.word_count = 0


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]
            curr.prefix_count += 1

        curr.word_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return 0
            else:
                curr = curr.children[ch]

        return curr.word_count

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root

        for ch in prefix:
            if ch not in curr.children:
                return 0
            else:
                curr = curr.children[ch]

        return curr.prefix_count

    def erase(self, word: str) -> None:
        if self.countWordsEqualTo(word) < 1:
            return

        curr = self.root

        for ch in word:
            curr = curr.children[ch]
            curr.prefix_count -= 1

        curr.word_count -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)

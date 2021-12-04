from collections import deque
from typing import List


class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()

            curr = curr.children[ch]

        curr.is_word = True


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.letters = deque()

        for w in words:
            self.trie.add(w[::-1])

    def query(self, letter: str) -> bool:
        self.letters.appendleft(letter)
        curr = self.trie.root

        for ch in self.letters:
            if ch in curr.children:
                curr = curr.children[ch]

                if curr.is_word:
                    return True
            else:
                return False

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

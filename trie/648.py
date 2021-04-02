from typing import List


class Node:
    def __init__(self):
        self.children = {}
        self.is_english_root = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word_root):
        curr = self.root

        for ch in word_root:
            if ch not in curr.children:
                curr.children[ch] = Node()

            curr = curr.children[ch]

        curr.is_english_root = True

    def search(self, word):
        path = []
        curr = self.root

        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
                path.append(ch)

                if curr.is_english_root:
                    return "".join(path)
            else:
                return word

        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        trie = Trie()

        for english_root in dictionary:
            trie.add(english_root)

        for i, word in enumerate(words):
            words[i] = trie.search(word)

        return " ".join(words)

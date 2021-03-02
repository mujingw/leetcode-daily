from collections import defaultdict
from typing import List


class Node:
    def __init__(self):
        self.children = dict()
        self.sentences = set()


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, sentence):
        curr = self.root

        for ch in sentence:
            if ch not in curr.children:
                curr.children[ch] = Node()

            curr = curr.children[ch]
            curr.sentences.add(sentence)

    def find(self, sentence):
        curr = self.root

        for ch in sentence:
            if ch not in curr.children:
                return set()

            curr = curr.children[ch]

        return curr.sentences


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentence_freq = defaultdict(int)
        self.trie = Trie()
        self.curr_input = ""
        self.TOP_K = 3

        for s, t in zip(sentences, times):
            self.sentence_freq[s] = t
            self.trie.add(s)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.sentence_freq[self.curr_input] += 1
            self.trie.add(self.curr_input)
            self.curr_input = ""

            return []
        else:
            self.curr_input += c
            res = list(self.trie.find(self.curr_input))
            res.sort(key=lambda x: (-self.sentence_freq[x], x))

            return res[:self.TOP_K]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

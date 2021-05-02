from collections import defaultdict
from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixes = defaultdict(set)
        self.suffixes = defaultdict(set)
        self.word2idx = dict()

        for idx, word in enumerate(words):
            for p in range(len(word) + 1):
                prefix = word[:p]
                suffix = word[p:]
                self.prefixes[prefix].add(word)
                self.suffixes[suffix].add(word)

            self.word2idx[word] = idx

    def f(self, prefix: str, suffix: str) -> int:
        idx = -1

        for word in self.prefixes[prefix] & self.suffixes[suffix]:
            idx = max(idx, self.word2idx[word])

        return idx

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix, suffix)

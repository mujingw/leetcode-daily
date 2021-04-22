from typing import List


class UF:
    def __init__(self, size):
        self.rank = [0] * size
        self.parent = [i for i in range(size)]

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)

        if self.rank[ru] < self.rank[rv]:
            self.parent[ru] = rv
        elif self.rank[rv] < self.rank[ru]:
            self.parent[rv] = ru
        else:
            self.parent[rv] = ru
            self.rank[ru] += 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        N1, N2 = len(words1), len(words2)

        if N1 != N2:
            return False

        word2num = {}

        for w1, w2 in pairs:
            if w1 not in word2num:
                word2num[w1] = len(word2num)

            if w2 not in word2num:
                word2num[w2] = len(word2num)

        uf = UF(len(word2num))

        for w1, w2 in pairs:
            u, v = word2num[w1], word2num[w2]
            uf.union(u, v)

        for w1, w2 in zip(words1, words2):
            if w1 == w2:
                continue

            if w1 not in word2num or w2 not in word2num:
                return False

            if uf.find(word2num[w1]) != uf.find(word2num[w2]):
                return False

        return True

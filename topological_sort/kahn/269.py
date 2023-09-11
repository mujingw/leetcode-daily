from collections import defaultdict, deque
from itertools import pairwise
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        self.words = words
        self.g = defaultdict(set)
        self.indeg = defaultdict(int)
        self.build_graph()
        self.get_indeg()
        q = deque([x for x in self.g if self.indeg[x] == 0])
        res = []

        while q:
            curr = q.popleft()
            res.append(curr)

            for neig in self.g[curr]:
                self.indeg[neig] -= 1

                if self.indeg[neig] == 0:
                    q.append(neig)

        return "".join(res) if len(res) == len(self.g) else ""

    def build_graph(self):
        for word in self.words:
            for ch in word:
                self.g[ch] = set()

        for w1, w2 in pairwise(self.words):
            processed_all = True

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    self.g[c1].add(c2)
                    processed_all = False
                    break

            if processed_all and len(w1) > len(w2):
                self.g = defaultdict(set)
                break

    def get_indeg(self):
        for v in self.g:
            for u in self.g[v]:
                self.indeg[u] += 1

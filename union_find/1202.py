from collections import deque, defaultdict
from typing import List


class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def add(self, x):
        if self.exist(x):
            return

        self.parent[x] = x
        self.rank[x] = 1

    def exist(self, x):
        return x in self.parent

    def union(self, u, v):
        ru, rv = self.find(u), self.find(v)

        if ru == rv:
            return

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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not pairs:
            return s

        p2n = defaultdict(deque)
        uf = UF()
        res = []

        for a, b in pairs:
            uf.add(a)
            uf.add(b)
            uf.union(a, b)

        for node in uf.parent:
            p2n[uf.find(node)].append(node)

        for k, v in p2n.items():
            p2n[k] = deque(sorted(list(v), key=lambda x: s[x]))

        for i in range(len(s)):
            if not uf.exist(i):
                res.append(s[i])
                continue

            q = p2n[uf.find(i)]
            res.extend(s[q.popleft()])

        return ''.join(res)

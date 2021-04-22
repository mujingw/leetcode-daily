from collections import defaultdict
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email2idx = {}
        idx2name = {}
        idx2emails = defaultdict(list)
        res = []

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                if email not in email2idx:
                    idx = len(email2idx)
                    email2idx[email] = idx
                    idx2name[idx] = name

        uf = UF(len(email2idx))

        for account in accounts:
            if len(account) >= 3:
                for email1, email2 in zip(account[1:], account[2:]):
                    uf.union(email2idx[email1], email2idx[email2])

        for email, idx in email2idx.items():
            idx2emails[uf.find(idx)].append(email)

        for idx, emails in idx2emails.items():
            record = [idx2name[idx]]
            record.extend(sorted(emails))
            res.append(record)

        return res

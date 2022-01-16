from collections import deque, defaultdict
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        N = len(nums)
        g = self.build_graph(sequences)
        in_degrees = self.get_indegrees(g)
        q = deque([x for x in range(1, N + 1) if in_degrees[x] == 0])
        count = 0

        while q:
            if len(q) > 1:
                return False

            curr = q.popleft()
            count += 1

            for neig in g[curr]:
                in_degrees[neig] -= 1

                if in_degrees[neig] == 0:
                    q.append(neig)

        return count == N

    def get_indegrees(self, g):
        in_degrees = defaultdict(int)

        for node in g:
            for neig in g[node]:
                in_degrees[neig] += 1

        return in_degrees

    def build_graph(self, seqs):
        g = defaultdict(set)

        for seq in seqs:
            for a, b in zip(seq, seq[1:]):
                g[a].add(b)

        return g

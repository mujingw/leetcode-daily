from collections import deque, defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succ_prob: List[float], start: int, end: int) -> float:
        g = defaultdict(set)

        for idx, (a, b) in enumerate(edges):
            g[a].add((b, idx))
            g[b].add((a, idx))

        q = deque([(start, 1.0)])
        seen = {start: 1.0}

        while q:
            curr, prob = q.popleft()

            for neig, idx in g[curr]:
                if neig not in seen or prob * succ_prob[idx] > seen[neig]:
                    seen[neig] = prob * succ_prob[idx]
                    q.append((neig, prob * succ_prob[idx]))

        return seen[end] if end in seen else 0.0

import collections
from collections import defaultdict
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = collections.deque([(0, 0)])
        seen = set([0])
        val_to_idx = defaultdict(list)

        for i, v in enumerate(arr):
            val_to_idx[v].append(i)

        while q:
            curr, dist = q.popleft()

            if curr == len(arr) - 1:
                return dist

            for next_pos in [curr + 1, curr - 1] + val_to_idx.pop(arr[curr], []):
                if next_pos not in seen and 0 <= next_pos < len(arr):
                    seen.add(next_pos)
                    q.append((next_pos, dist + 1))

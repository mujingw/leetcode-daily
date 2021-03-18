from collections import defaultdict
from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        d = defaultdict(int)

        for s, e in slots1 + slots2:
            d[s] += 1
            d[e] -= 1

        N = len(d)
        total = 0
        all_points = sorted(d.keys())

        for i, t in enumerate(all_points):
            total += d[t]

            if total == 2:
                if i != N - 1:
                    if t + duration <= all_points[i + 1]:
                        return [t, t + duration]

        return []

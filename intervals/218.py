from collections import defaultdict
from typing import List

from sortedcontainers import SortedDict


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        res = []
        d = defaultdict(list)
        prev_h = 0
        sd = SortedDict()

        for l, r, h in buildings:
            d[l].append((l, h, 1))
            d[r].append((r, h, -1))

        for x in sorted(d.keys()):
            for loc, height, typ in d[x]:
                if typ == 1:
                    if height not in sd:
                        sd[height] = 1
                    else:
                        sd[height] += 1
                else:
                    if sd[height] == 1:
                        del sd[height]
                    else:
                        sd[height] -= 1

            curr_h = sd.peekitem(-1)[0] if sd else 0

            if curr_h != prev_h:
                res.append([x, curr_h])
                prev_h = curr_h

        return res

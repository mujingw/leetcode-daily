import collections
from collections import defaultdict
from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], eid: int) -> int:
        imp = {}
        g = defaultdict(set)
        res = 0

        for emp in employees:
            imp[emp.id] = emp.importance

            for ee in emp.subordinates:
                g[emp.id].add(ee)

        q = collections.deque([eid])

        while q:
            curr = q.popleft()
            res += imp[curr]

            for sub in g[curr]:
                q.append(sub)

        return res

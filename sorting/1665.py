from typing import List


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        res = 0

        for actual, minimum in sorted(tasks, key=lambda x: (x[1] - x[0])):
            res = max(res + actual, minimum)

        return res

from typing import List

from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        res = []

        for v in nums[::-1]:
            res.append(sl.bisect_left(v))
            sl.add(v)

        return res[::-1]

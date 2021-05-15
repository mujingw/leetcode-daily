from typing import List


class Solution:
    def maxSatisfaction(self, arr: List[int]) -> int:
        arr.sort()
        res = 0
        pos = len(arr) - 1
        delta = arr[pos]

        while pos >= 0 and delta > 0:
            res += delta
            pos -= 1

            if pos >= 0:
                delta += arr[pos]

        return res

from typing import List


class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        desc = []
        res = 0

        for i, num in enumerate(A):
            if not desc or A[desc[-1]] > num:
                desc.append(i)

        for r in range(len(A) - 1, -1, -1):
            while desc and A[r] >= A[desc[-1]]:
                res = max(res, r - desc[-1])
                desc.pop()

        return res

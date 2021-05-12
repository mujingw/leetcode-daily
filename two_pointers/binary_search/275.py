from typing import List


class Solution:
    def hIndex(self, arr: List[int]) -> int:
        N = len(arr)
        l, r = 0, N

        while l < r:
            mid = (l + r) // 2
            citations = arr[mid]
            papers = N - mid

            if papers == citations:
                return papers
            elif papers < citations:
                r = mid
            else:
                l = mid + 1

        return N - l

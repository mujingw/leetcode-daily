from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        N = len(arr)
        lb, rb = 0, N - 1

        while lb < N - 1 and arr[lb] <= arr[lb + 1]:
            lb += 1

        while rb > 0 and arr[rb] >= arr[rb - 1]:
            rb -= 1

        if lb >= rb:
            return 0

        res = min(rb, N - lb - 1)
        l, r = 0, rb

        while l <= lb and r <= N - 1:
            if arr[l] <= arr[r]:
                res = min(res, r - l - 1)
                l += 1
            else:
                r += 1

        return res

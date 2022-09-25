from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        N = len(arr)
        up, down = [0] * N, [0] * N
        res = 0

        for i in range(1, N):
            if arr[i] > arr[i - 1]:
                up[i] = up[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                down[i] = down[i + 1] + 1

        for i in range(1, N - 1):
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                res = max(res, up[i] + down[i] + 1)

        return res

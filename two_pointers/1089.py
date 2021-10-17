from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        zeroes = arr.count(0)
        dest_idx = N + zeroes - 1

        for src_idx in range(N - 1, -1, -1):
            if arr[src_idx] == 0:
                self.try_copy(arr, src_idx, dest_idx, N)
                dest_idx -= 1
                self.try_copy(arr, src_idx, dest_idx, N)
            else:
                self.try_copy(arr, src_idx, dest_idx, N)

            dest_idx -= 1

    def try_copy(self, arr, from_idx, to_idx, size):
        if to_idx < size:
            arr[to_idx] = arr[from_idx]

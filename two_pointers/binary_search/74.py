from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        l, r = 0, R * C

        while l < r:
            mid = (l + r) // 2

            if matrix[mid // C][mid % C] < target:
                l = mid + 1
            else:
                r = mid

        return 0 <= l < R * C and matrix[l // C][l % C] == target

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        end = float("-inf")
        arrows = 0

        for s, e in sorted(points, key=lambda x: x[1]):
            if s > end:
                arrows += 1
                end = e

        return arrows

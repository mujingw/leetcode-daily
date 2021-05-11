from typing import List


class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        width = len(arr) - k
        total = min_score = score = sum(arr[:width])
        p = width

        while p < len(arr):
            total += arr[p]
            score += arr[p]
            score -= arr[p - width]
            min_score = min(score, min_score)
            p += 1

        return total - min_score

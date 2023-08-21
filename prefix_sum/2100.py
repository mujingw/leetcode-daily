from typing import List


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        N = len(security)
        left, right = [1] * N, [1] * N
        res = []

        for i in range(1, N):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if security[i] <= security[i + 1]:
                right[i] = right[i + 1] + 1

        for i in range(time, N - time):
            if left[i] >= time + 1 and right[i] >= time + 1:
                res.append(i)

        return res

from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        s = []

        for i, t in enumerate(T):
            while s and s[-1][0] < t:
                temperature, idx = s.pop()
                res[idx] = i - idx

            s.append((t, i))

        return res

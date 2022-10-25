from typing import List


class Solution:
    def dailyTemperatures(self, tprts: List[int]) -> List[int]:
        stack, res = [], [0 for _ in range(len(tprts))]

        for i, t in enumerate(tprts):
            while stack and tprts[stack[-1]] < t:
                res[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return res

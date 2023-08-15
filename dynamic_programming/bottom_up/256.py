from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        R, B, G = 0, 1, 2
        N = len(costs)
        red = [costs[0][R]] * N
        blue = [costs[0][B]] * N
        green = [costs[0][G]] * N

        for i in range(1, N):
            red[i] = min(blue[i-1], green[i-1]) + costs[i][R]
            blue[i] = min(red[i-1], green[i-1]) + costs[i][B]
            green[i] = min(red[i-1], blue[i-1]) + costs[i][G]

        return min(red[-1], blue[-1], green[-1])

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        red = [float('inf')] * N
        blue = [float('inf')] * N
        green = [float('inf')] * N
        red[0] = costs[0][0]
        blue[0] = costs[0][1]
        green[0] = costs[0][2]

        for i in range(1, N):
            red[i] = min(blue[i-1], green[i-1]) + costs[i][0]
            blue[i] = min(red[i-1], green[i-1]) + costs[i][1]
            green[i] = min(blue[i-1], red[i-1]) + costs[i][2]

        return int(min(red[-1], blue[-1], green[-1]))

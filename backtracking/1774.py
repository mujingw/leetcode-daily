from typing import List


class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        def dfs(res, curr, toppings, pos):
            res.append(curr)

            if pos == len(toppings):
                return

            dfs(res, curr, toppings, pos + 1)
            dfs(res, curr + toppings[pos], toppings, pos + 1)
            dfs(res, curr + toppings[pos] * 2, toppings, pos + 1)

        res = []

        for base in baseCosts:
            dfs(res, base, toppingCosts, 0)

        return min([(abs(cost - target), cost) for cost in res])[1]

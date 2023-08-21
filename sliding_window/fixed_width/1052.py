from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        already_happy, curr_impr, most_impr = 0, 0, 0

        for i, (c, g) in enumerate(zip(customers, grumpy)):
            if g == 0:
                already_happy += c

            curr_impr += c * g

            if i >= X:
                curr_impr -= customers[i - X] * grumpy[i - X]

            most_impr = max(most_impr, curr_impr)

        return already_happy + most_impr

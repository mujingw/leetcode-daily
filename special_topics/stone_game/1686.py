from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        points = sorted([(a + b, i, a, b) for i, (a, b) in enumerate(zip(aliceValues, bobValues))], reverse=True)
        alice = sum(a for i, (x, idx, a, b) in enumerate(points) if i % 2 == 0)
        bob = sum(b for i, (x, idx, a, b) in enumerate(points) if i % 2 == 1)

        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0

from collections import defaultdict
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = defaultdict(int)
        total = 0

        for passengers, start, end in trips:
            car[start] += passengers
            car[end] -= passengers

        for pos in sorted(car.keys()):
            total += car[pos]

            if total > capacity:
                return False

        return True

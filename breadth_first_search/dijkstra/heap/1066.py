from collections import defaultdict
from heapq import heappush, heappop
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        pq = [(0, 0, '0' * len(bikes))]
        seen = defaultdict(lambda: float('inf'))

        while pq:
            cost, i, bike_status = heappop(pq)

            if i == len(workers):
                return cost

            for j, bike in enumerate(bikes):
                if bike_status[j] != '1':
                    new_cost = cost + self.manhattan(workers[i], bike)
                    new_bike_status = bike_status[:j] + '1' + bike_status[j + 1:]

                    if new_cost < seen[(i + 1, new_bike_status)]:
                        seen[(i + 1, new_bike_status)] = new_cost
                        heappush(pq, (new_cost, i + 1, new_bike_status))

        return -1

    def manhattan(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

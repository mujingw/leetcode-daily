from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        candidates = sorted(zip(efficiency, speed), key=lambda x: x[0], reverse=True)
        speed_heap = []
        speed_sum, res = 0, 0

        for curr_efficiency, curr_speed in candidates:
            if len(speed_heap) > k - 1:
                speed_sum -= heappop(speed_heap)

            heappush(speed_heap, curr_speed)
            speed_sum += curr_speed
            res = max(res, speed_sum * curr_efficiency)

        return res % MOD

from collections import deque
from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        e1 = deque(encoded1)
        e2 = deque(encoded2)
        res = []

        while e1 and e2:
            val1, freq1 = e1.popleft()
            val2, freq2 = e2.popleft()
            prod = val1 * val2

            if freq1 == freq2:
                if res and res[-1][0] == prod:
                    res[-1][1] += freq1
                else:
                    res.append([prod, freq1])
            elif freq1 > freq2:
                if res and res[-1][0] == prod:
                    res[-1][1] += freq2
                else:
                    res.append([prod, freq2])

                e1.appendleft([val1, freq1 - freq2])
            else:
                if res and res[-1][0] == prod:
                    res[-1][1] += freq1
                else:
                    res.append([prod, freq1])

                e2.appendleft([val2, freq2 - freq1])

        return res

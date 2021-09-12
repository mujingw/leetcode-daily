from collections import deque
from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        q = deque(initialBoxes)
        seen = set(initialBoxes)
        res = 0
        on_hold = set([])
        all_keys = set([])

        while q:
            curr = q.popleft()
            res += candies[curr]
            all_keys.update(set(keys[curr]))

            potential_new_boxes = all_keys.intersection(on_hold)

            for box in potential_new_boxes:
                if box not in seen and status[box] == 0:
                    seen.add(box)
                    q.append(box)

            for box in list(on_hold):
                if box in seen:
                    on_hold.remove(box)

            for box in containedBoxes[curr]:
                if (box in all_keys or status[box] == 1) and box not in seen:
                    q.append(box)
                    seen.add(box)
                elif status[box] == 0 and box not in seen:
                    on_hold.add(box)

        return res

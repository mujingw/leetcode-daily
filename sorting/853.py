from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(pos, sp) for pos, sp in zip(position, speed)], reverse=True)
        front_pos, front_sp = cars[0]
        count = 1

        for pos, sp in cars[1:]:
            h = (target - front_pos) / front_sp

            if sp * h + pos < target:
                front_pos, front_sp = pos, sp
                count += 1

        return count

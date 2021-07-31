from heapq import heappush, heappop
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        h, time = [], 0

        for duration, last in courses:
            if time + duration <= last:
                heappush(h, -duration)
                time += duration
            elif h and -h[0] > duration:
                time += (duration - (-heappop(h)))
                heappush(h, -duration)

        return len(h)

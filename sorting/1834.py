from collections import deque
from heapq import heappush, heappop
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        my_tasks = [(idx, enq, pt) for idx, (enq, pt) in enumerate(tasks)]
        tasks_by_time = deque(sorted(my_tasks, key=lambda x: (x[1])))
        res = []
        time = 0
        N = len(tasks)
        h = []

        while len(res) < N:
            if not h and time < tasks_by_time[0][1]:
                time = tasks_by_time[0][1]

            while tasks_by_time and tasks_by_time[0][1] <= time:
                idx, enq, pt = tasks_by_time.popleft()
                heappush(h, (pt, idx))

            if h:
                pt, idx = heappop(h)
                time += pt
                res.append(idx)

        return res

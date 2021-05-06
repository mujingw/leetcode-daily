from collections import defaultdict


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        agg_schedule = defaultdict(int)
        total = 0
        res = []
        curr_start = float('-inf')

        for emp_schedule in schedule:
            for interval in emp_schedule:
                agg_schedule[interval.start] += 1
                agg_schedule[interval.end] -= 1

        for time in sorted(agg_schedule.keys()):
            prev = total
            total += agg_schedule[time]

            if prev == 0 and total > 0:
                res.append(Interval(curr_start, time))

            if prev > 0 and total == 0:
                curr_start = time

        return res[1:]

from collections import defaultdict
from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        def build_intervals(s):
            ch2start = defaultdict(int)
            ch2end = defaultdict(int)
            N = len(s)

            for i in range(N - 1, -1, -1):
                ch2start[s[i]] = i

            for i in range(N):
                ch2end[s[i]] = i

            intervals = []

            for ch in set(s):
                start, end = ch2start[ch], ch2end[ch]
                p = start

                while p <= end and start == ch2start[ch]:
                    start = min(start, ch2start[s[p]])
                    end = max(end, ch2end[s[p]])
                    p += 1

                if start == ch2start[ch]:
                    intervals.append((start, end))

            return intervals

        def sorted_merge(intervals):
            intervals.sort(key=lambda x: x[1])
            res = [[intervals[0][0], intervals[0][1]]]

            for s, e in intervals[1:]:
                if s > res[-1][1]:
                    res.append([s, e])

            return res

        return [s[start:end + 1] for start, end in sorted_merge(build_intervals(s))]

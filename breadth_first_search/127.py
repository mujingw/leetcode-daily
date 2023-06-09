import string
from collections import deque
from typing import List


class Solution:
    def ladderLength(self, start: str, end: str, wl: List[str]) -> int:
        ws = set(wl)
        q = deque([(start, 1)])
        seen = {start}

        while q:
            curr, steps = q.popleft()

            if curr == end:
                return steps

            for i in range(len(curr)):
                for ch in string.ascii_lowercase:
                    next_word = curr[:i] + ch + curr[i + 1:]

                    if next_word in ws and next_word not in seen:
                        seen.add(next_word)
                        q.append((next_word, steps + 1))

        return 0

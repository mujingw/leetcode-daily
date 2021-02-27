import collections
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        s = []
        pushed = collections.deque(pushed)
        popped = collections.deque(popped)

        while pushed:
            s.append(pushed.popleft())

            while s and s[-1] == popped[0]:
                s.pop()
                popped.popleft()

            if not popped:
                break

        return len(s) == 0

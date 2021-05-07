from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0

            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                if count < 0:
                    return False

            return count == 0

        q = deque([s])
        seen = {s}

        while q:
            size = len(q)
            valid_s = []

            for _ in range(size):
                curr = q.popleft()

                if is_valid(curr):
                    valid_s.append(curr)

                for i in range(len(curr)):
                    next_s = curr[:i] + curr[i + 1:]

                    if next_s not in seen:
                        q.append(next_s)
                        seen.add(next_s)

            if len(valid_s) > 0:
                return valid_s

from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        q = deque([s])
        seen = {s}

        while q:
            size = len(q)
            valid_strings = []

            for _ in range(size):
                curr = q.popleft()

                if self.is_valid(curr):
                    valid_strings.append(curr)
                    continue

                for i in range(len(curr)):
                    next_string = curr[:i] + curr[i + 1:]

                    if next_string not in seen:
                        q.append(next_string)
                        seen.add(next_string)

            if valid_strings:
                return valid_strings

    def is_valid(self, s):
        count = 0

        for ch in s:
            if ch == '(':
                count += 1
            elif ch == ')':
                count -= 1

            if count < 0:
                return False

        return count == 0

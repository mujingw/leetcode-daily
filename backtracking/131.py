from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtrack(res, [], s, 0)

        return res

    def backtrack(self, res, curr, s, pos):
        if pos == len(s):
            res.append(curr[:])
            return

        for i in range(pos, len(s)):
            candidate = s[pos:i+1]

            if candidate == candidate[::-1]:
                curr.append(candidate)
                self.backtrack(res, curr, s, i+1)
                curr.pop()

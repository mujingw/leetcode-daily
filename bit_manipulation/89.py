from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]

        res = [0, 1]

        for i in range(1, n):
            curr = []

            for code in res[::-1]:
                curr.append((1 << i) ^ code)

            res.extend(curr)

        return res

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0, 1]

        for i in range(1, n):
            mask = 1 << i
            curr = []

            for code in res[::-1]:
                curr.append(mask ^ code)

            res.extend(curr)

        return res

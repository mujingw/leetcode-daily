from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def ok(at_least):
            curr_total, cuts = 0, 0

            for s in sweetness:
                if curr_total >= at_least and cuts < K:
                    cuts += 1
                    curr_total = s
                else:
                    curr_total += s

            return curr_total >= at_least and cuts == K

        l, r = min(sweetness), 10 ** 9 + 1

        while l < r:
            mid = (l + r) // 2

            if ok(mid):
                l = mid + 1
            else:
                r = mid

        if ok(l):
            return l
        else:
            return l - 1

from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        l, r = min(sweetness), 10 ** 9 + 1

        while l < r:
            mid = (l + r) // 2

            if self.ok(mid, sweetness, k):
                l = mid + 1
            else:
                r = mid

        return l if self.ok(l, sweetness, k) else l - 1

    def ok(self, at_least, sweetness, K):
        curr_total, cuts = 0, 0

        for s in sweetness:
            if curr_total >= at_least and cuts < K:
                cuts += 1
                curr_total = s
            else:
                curr_total += s

        return curr_total >= at_least and cuts == K

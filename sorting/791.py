from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d_order = defaultdict(lambda: 26)

        for i, v in enumerate(order):
            d_order[v] = i

        return "".join(sorted(list(s), key=lambda x: d_order[x]))

from collections import defaultdict


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d_order = defaultdict(int)

        for i, v in enumerate(order):
            d_order[v] = i + 1

        return "".join(sorted(list(s), key=lambda x: d_order[x]))

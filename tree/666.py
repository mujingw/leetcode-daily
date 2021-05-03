from collections import defaultdict
from typing import List


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        sum_at_node = defaultdict(int)
        node_appearances = defaultdict(int)

        for num in nums[::-1]:
            lvl, pos, val = num // 100, num // 10 % 10, num % 10
            node_appearances[lvl, pos] = max(1, node_appearances[lvl + 1, pos * 2 - 1] + node_appearances[
                lvl + 1, pos * 2])
            sum_at_node[lvl, pos] = sum_at_node[lvl + 1, pos * 2 - 1] \
                + sum_at_node[lvl + 1, pos * 2] \
                + node_appearances[lvl, pos] * val

        return sum_at_node[1, 1]

from heapq import heappush, heappop


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.longest = 0
        self.dfs(root)

        return self.longest

    def dfs(self, node):
        if not node:
            return 0

        h = []

        for child in node.children:
            heappush(h, -self.dfs(child))

        if len(h) > 1:
            a = -heappop(h)
            b = -heappop(h)
            self.longest = max(self.longest, a + b)

            return max(a, b) + 1
        elif len(h) == 1:
            self.longest = max(self.longest, -h[0])

            return -h[0] + 1
        else:
            return 1

from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        d = {node: Node(node.val)}
        q = deque([node])
        seen = {node}

        while q:
            curr = q.popleft()

            for neig in curr.neighbors:
                if neig not in seen:
                    d[neig] = Node(neig.val)
                    q.append(neig)
                    seen.add(neig)

                d[curr].neighbors.append(d[neig])

        return d[node]

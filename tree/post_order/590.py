# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        stack, res = [root, root], []

        while stack:
            curr = stack.pop()

            if stack and stack[-1] == curr:
                for c in curr.children[::-1]:
                    stack.append(c)
                    stack.append(c)
            else:
                res.append(curr.val)

        return res

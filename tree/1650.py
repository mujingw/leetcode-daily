class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents = set([])
        curr = p

        while curr:
            parents.add(curr)
            curr = curr.parent

        curr = q

        while curr:
            if curr in parents:
                return curr
            else:
                parents.add(curr)
                curr = curr.parent

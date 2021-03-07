class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        cp, cq = p, q

        while cp != cq:
            cp = cp.parent
            cq = cq.parent

            if cp is None:
                cp = q

            if cq is None:
                cq = p

        return cp

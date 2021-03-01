class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            if not root:
                return None

            if p.val > q.val:
                return lca(root, q, p)

            if root.val < p.val:
                return lca(root.right, p, q)
            elif root.val > q.val:
                return lca(root.left, p, q)
            else:
                return root

        return lca(root, p, q)

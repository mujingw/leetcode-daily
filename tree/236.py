class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            if not root:
                return None

            if root == p or root == q:
                return root
            else:
                left = lca(root.left, p, q)
                right = lca(root.right, p, q)

                if left and right:
                    return root
                elif left and not right:
                    return left
                elif right and not left:
                    return right

        return lca(root, p, q)

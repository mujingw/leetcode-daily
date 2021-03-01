class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def lca(root, p, q):
            if not root:
                return None

            if root == p or root == q:
                return root

            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            if left and right:
                return root

            return left if left else right

        if len(nodes) == 1:
            return nodes[0]

        res = lca(root, nodes[0], nodes[1])

        for node in nodes:
            res = lca(root, res, node)

        return res

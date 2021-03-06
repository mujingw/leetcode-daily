class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def lca(root, nodes):
            if not root:
                return None

            if root in nodes:
                return root

            l = lca(root.left, nodes)
            r = lca(root.right, nodes)

            if l and r:
                return root
            else:
                return l if l else r

        return lca(root, set(nodes))

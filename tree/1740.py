class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def lca(root, p, q):
            if not root:
                return None

            if root.val == p or root.val == q:
                return root

            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            if left and right:
                return root

            if left:
                return left

            if right:
                return right

        def find_node(root, p, depth):
            if not root:
                return -1

            if root.val == p:
                return depth
            else:
                left = find_node(root.left, p, depth + 1)
                right = find_node(root.right, p, depth + 1)

                if left != -1:
                    return left
                elif right != -1:
                    return right
                else:
                    return -1

        lca_node = lca(root, p, q)

        return find_node(lca_node, p, 0) + find_node(lca_node, q, 0)

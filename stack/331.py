class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []

        for node in preorder.split(","):
            while stack and stack[-1] == '#' == node:
                stack.pop()

                if not stack:
                    return False

                stack.pop()

            stack.append(node)

        return len(stack) == 1 and stack[0] == '#'

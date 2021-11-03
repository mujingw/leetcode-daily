class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append((ch, i))
            elif ch == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((ch, i))

        bad_indices = set([i for ch, i in stack])

        return ''.join([ch for i, ch in enumerate(s) if i not in bad_indices])

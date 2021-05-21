class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = list(s)

        for i, ch in enumerate(s):
            if ch in '()':
                if not stack:
                    stack.append((ch, i))
                else:
                    if stack[-1][0] == '(' and ch == ')':
                        stack.pop()
                    else:
                        stack.append((ch, i))

        for ch, i in stack:
            res[i] = ""

        return "".join(res)

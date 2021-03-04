class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            if not stack:
                stack.append((ch, 1))
            else:
                prev_ch, count = stack[-1]

                if prev_ch == ch:
                    stack.append((ch, count + 1))
                else:
                    stack.append((ch, 1))

            if stack and stack[-1][1] == k:
                p = k

                while p > 0:
                    stack.pop()
                    p -= 1

        return "".join([ch for ch, count in stack])

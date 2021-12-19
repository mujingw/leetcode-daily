class Solution:
    def decodeString(self, s: str) -> str:
        sb, k = [], 0
        stack = []

        for ch in s:
            if ch.isdigit():
                k = (k * 10) + int(ch)
            elif ch == '[':
                stack.append((sb, k))
                sb, k = [], 0
            elif ch == ']':
                prev_sb, prev_k = stack.pop()
                sb = prev_sb + prev_k * sb
            else:
                sb.append(ch)

        return ''.join(sb)

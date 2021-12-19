from collections import deque


class Solution:
    def decodeString(self, s: str) -> str:
        return ''.join(self.dfs(deque(list(s))))

    def dfs(self, q):
        sb, k = [], 0

        while q:
            ch = q.popleft()

            if ch.isdigit():
                k = k * 10 + int(ch)
            elif ch == '[':
                next_chunk = self.dfs(q)
                sb.extend(next_chunk * k)
                k = 0
            elif ch == ']':
                break
            else:
                sb.append(ch)

        return sb

from collections import deque


class Solution:
    def canReach(self, s: str, min_jump: int, max_jump: int) -> bool:
        q = deque([0])
        N = len(s)
        max_seen = 0

        while q:
            curr = q.popleft()

            if curr == N - 1:
                return True

            closest = max(max_seen, curr + min_jump)
            farthest = min(N - 1, curr + max_jump)

            for next_step in range(closest, farthest + 1):
                if s[next_step] == '0':
                    q.append(next_step)

            max_seen = max(max_seen, farthest)

        return False

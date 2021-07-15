class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)

        def dfs(res, pos, seen):
            if pos == N:
                res.append(len(seen))
                return

            for i in range(pos + 1, N + 1):
                if s[pos:i] not in seen:
                    seen.add(s[pos:i])
                    dfs(res, i, seen)
                    seen.remove(s[pos:i])

        res = []
        dfs(res, 0, set())

        return max(res)

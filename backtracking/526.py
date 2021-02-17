def countArrangement(self, n: int) -> int:
    def dfs(res, curr, pos, n, used):
        if len(curr) == n:
            res[0] += 1

            return

        for i in range(1, n + 1):
            if used[i]:
                continue

            if i % pos == 0 or pos % i == 0:
                used[i] = True
                curr.append(i)
                dfs(res, curr, pos + 1, n, used)
                curr.pop()
                used[i] = False

    res = [0]
    used = [False] * (n + 1)
    dfs(res, [], 1, n, used)

    return res[0]

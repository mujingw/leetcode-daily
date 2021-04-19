class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(res, curr, tiles, used):
            if curr:
                res[0] += 1

            for i in range(N):
                if used[i]:
                    continue

                if i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:
                    continue

                curr.append(tiles[i])
                used[i] = True
                dfs(res, curr, tiles, used)
                used[i] = False
                curr.pop()

        res = [0]
        N = len(tiles)
        used = [False] * N
        dfs(res, [], sorted(tiles), used)

        return res[0]

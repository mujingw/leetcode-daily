class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(res, curr, l, r, n):
            if l > r or l < 0:
                return

            if len(curr) == 2 * n:
                res.append(curr)
                return

            dfs(res, curr + "(", l - 1, r, n)
            dfs(res, curr + ")", l, r - 1, n)

        res = []
        dfs(res, "", n, n, n)

        return res

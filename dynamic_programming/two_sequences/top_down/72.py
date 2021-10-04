class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.dfs(word1, word2, {})

    def dfs(self, w1, w2, memo):
        if not w1:
            return len(w2)

        if not w2:
            return len(w1)

        if (w1, w2) in memo:
            return memo[(w1, w2)]

        res = 0

        if w1[-1] == w2[-1]:
            res = self.dfs(w1[:-1], w2[:-1], memo)
        else:
            adjust_w1 = self.dfs(w1[:-1], w2, memo)
            adjust_w2 = self.dfs(w1, w2[:-1], memo)
            adjust_both = self.dfs(w1[:-1], w2[:-1], memo)
            res = min(adjust_w1, adjust_w2, adjust_both) + 1

        memo[(w1, w2)] = res

        return res

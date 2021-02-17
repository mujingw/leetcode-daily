class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def dfs(res, curr, k, needed, start):
            if needed < 0 or len(curr) > k:
                return

            if len(curr) == k and needed == 0:
                res.append(curr[:])

                return

            for num in range(start, 10):
                curr.append(num)
                dfs(res, curr, k, needed - num, num + 1)
                curr.pop()

        res = []
        dfs(res, [], k, n, 1)

        return res

from typing import List


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def dfs(res, curr, word):
            if not word:
                res.append(curr)

                return

            dfs(res, curr + word[0], word[1:])

            if curr and curr[-1].isdigit():
                dfs(res, curr[:-1] + str(int(curr[-1]) + 1), word[1:])
            else:
                dfs(res, curr + "1", word[1:])

        res = []
        dfs(res, "", word)

        return res
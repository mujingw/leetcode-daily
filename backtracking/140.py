from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        def helper(s):
            res = []

            if s in w_dict:
                res.append(s)

            for i in range(1, len(s)):
                right = s[i:]

                if right in w_dict:
                    res.extend([left + " " + right for left in helper(s[0:i])])

            return res

        w_dict = set(wordDict)

        return helper(s)

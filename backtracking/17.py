class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        def dfs(res, curr, digits, pos, phone):
            if pos == len(digits):
                res.append(curr)

                return

            for letter in phone[digits[pos]]:
                dfs(res, curr + letter, digits, pos + 1, phone)

        phone = {"2": "abc", "3": "def", \
                 "4": "ghi", "5": "jkl", "6": "mno", \
                 "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []

        if not digits:
            return res

        dfs(res, "", digits, 0, phone)

        return res

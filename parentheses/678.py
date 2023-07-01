class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.ok('(', s) and self.ok(')', s[::-1])

    def ok(self, opening_chr, s):
        count = 0

        for ch in s:
            if ch == opening_chr or ch == '*':
                count += 1
            else:
                count -= 1

            if count < 0:
                return False

        return True

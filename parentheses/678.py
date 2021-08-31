class Solution:
    def checkValidString(self, s: str) -> bool:
        max_right_allowed = 0
        min_right_needed = 0

        for ch in s:
            if ch == '(':
                max_right_allowed += 1
                min_right_needed += 1
            elif ch == ')':
                max_right_allowed -= 1
                min_right_needed -= 1
            else:
                max_right_allowed += 1
                min_right_needed -= 1

            if max_right_allowed < 0:
                return False

            if min_right_needed < 0:
                min_right_needed = 0

        return min_right_needed == 0

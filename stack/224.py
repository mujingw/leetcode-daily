class Solution:
    def calculate(self, s: str) -> int:
        preceding_sign, res, num, stack = 1, 0, 0, []

        for ch in s + '+':
            if ch.isspace():
                continue

            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
            else:
                if ch in "+-":
                    res += preceding_sign * num
                    preceding_sign = 1 if ch == '+' else -1
                elif ch == '(':
                    stack.append((res, preceding_sign))
                    res, preceding_sign = 0, 1
                elif ch == ')':
                    res += preceding_sign * num
                    last_level_res, last_level_sign = stack.pop()
                    res = (last_level_res + last_level_sign * res)

                num = 0

        return res

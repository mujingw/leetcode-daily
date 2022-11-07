class Solution:
    def calculate(self, s: str) -> int:
        sign, res, num, stack = 1, 0, 0, []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
            elif ch.isspace():
                continue
            else:
                if ch == '+':
                    res += sign * num
                    sign = 1
                elif ch == '-':
                    res += sign * num
                    sign = -1
                elif ch == '(':
                    stack.append((res, sign))
                    res, sign = 0, 1
                elif ch == ')':
                    res += sign * num
                    prev_res, prev_sign = stack.pop()
                    res = (res * prev_sign + prev_res)

                num = 0

        return res + num * sign

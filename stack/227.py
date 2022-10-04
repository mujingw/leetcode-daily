class Solution:
    def calculate(self, s: str) -> int:
        s = s + '+'
        preceding_op, num = '+', 0
        stack = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
            elif ch.isspace():
                continue
            else:
                if preceding_op == '+':
                    stack.append(num)
                elif preceding_op == '-':
                    stack.append(-num)
                elif preceding_op == '*':
                    last_num = stack.pop()
                    stack.append(last_num * num)
                elif preceding_op == '/':
                    last_num = stack.pop()
                    stack.append(int(last_num / num))

                preceding_op = ch
                num = 0

        return sum(stack)

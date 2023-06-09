class Solution:
    def calculate(self, s: str) -> int:
        stack, num, pre_op = [], 0, '+'

        for ch in s + '+':
            if ch.isspace():
                continue

            if ch.isdigit():
                num = num * 10 + ord(ch) - ord('0')
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                else:
                    x = stack.pop()

                    if pre_op == '*':
                        stack.append(x * num)
                    elif pre_op == '/':
                        stack.append(int(x / num))

                num, pre_op = 0, ch

        return sum(stack)

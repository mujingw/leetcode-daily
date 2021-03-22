class Solution:
    def calculate(self, s: str) -> int:
        def get_int_chunk(p, start_ch, s, N):
            num = int(start_ch)

            while p < N and s[p].isdigit():
                num = (num * 10 + int(s[p]))
                p += 1

            return num, p

        N, sign, res = len(s), 1, 0
        stack = []
        p = 0

        while p < N:
            ch = s[p]
            p += 1

            if ch.isdigit():
                num, p = get_int_chunk(p, ch, s, N)
                res += (num * sign)
            elif ch == '+':
                sign = 1
            elif ch == '-':
                sign = -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                res = (res * stack.pop() + stack.pop())

        return res

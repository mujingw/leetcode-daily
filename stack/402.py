class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        s = []

        for ch in num:
            while k > 0 and s and int(s[-1]) > int(ch):
                s.pop()
                k -= 1

            s.append(ch)

        while k > 0 and s:
            s.pop()
            k -= 1

        res = "".join(s).lstrip("0")

        return res if res != "" else "0"

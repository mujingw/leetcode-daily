class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        M, N = len(word), len(abbr)
        p, q = 0, 0

        while p < M and q < N:
            if word[p] == abbr[q]:
                p += 1
                q += 1
            elif abbr[q].isalpha():
                return False
            elif abbr[q] == '0':
                return False
            else:
                end = q

                while end < N and abbr[end].isnumeric():
                    end += 1

                count = int(abbr[q:end])
                p += count
                q = end

        return p == M and q == N

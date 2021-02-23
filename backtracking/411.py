from typing import List


class Solution:
    def valid_word_abbr(self, word, abbr):
        i, j = 0, 0
        m, n = len(word), len(abbr)

        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isnumeric():
                k = j

                while k < n and abbr[k].isnumeric():
                    k += 1

                i += int("".join(abbr[j:k]))
                j = k
            else:
                return False

        return i == m and j == n

    def get_len(self, abbr):
        count = 0

        for i, ch in enumerate(abbr):
            if i > 0 and abbr[i].isdigit() and abbr[i - 1].isdigit():
                continue
            else:
                count += 1

        return count

    def gen_abbrs(self, word, d):
        def dfs(res, curr, pos, word, count):
            if len(curr) > self.min_len:
                return

            if pos == len(word):
                abbr = curr + [str(count)] if count > 0 else curr

                if all([not self.valid_word_abbr(w, abbr) for w in d]):
                    self.min_len = self.get_len(abbr)
                    res.append(abbr)

                return

            if count > 0:
                dfs(res, curr + [str(count)] + [word[pos]], pos + 1, word, 0)
            else:
                dfs(res, curr + [word[pos]], pos + 1, word, 0)

            dfs(res, curr, pos + 1, word, count + 1)

        res = []
        self.min_len = float("inf")
        dfs(res, [], 0, word, 0)

        return res

    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        d = [word for word in dictionary if len(word) == len(target)]
        all_abbrs = sorted(self.gen_abbrs(target, d), key=lambda x: self.get_len(x))

        return "".join(all_abbrs[0])

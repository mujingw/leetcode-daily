from typing import List
from collections import deque


class Solution:
    def valid_word_abbr(self, word, abbr):
        q1 = deque(list(word))
        q2 = deque(abbr)

        while q1 and q2:
            c1, c2 = q1.popleft(), q2.popleft()

            if c1 == c2:
                continue

            elif c2.isdigit():
                count = int(c2)

                if count == 0:
                    return False

                while q2 and q2[0].isdigit():
                    count = (count * 10 + int(q2.popleft()))

                for i in range(count - 1):
                    if q1:
                        q1.popleft()
                    else:
                        return False
            else:
                return False

        return not q1 and not q2

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
        d = [word for word in set(dictionary) if len(word) == len(target)]
        all_abbrs = sorted(self.gen_abbrs(target, d), key=lambda x: self.get_len(x))

        return "".join(all_abbrs[0])

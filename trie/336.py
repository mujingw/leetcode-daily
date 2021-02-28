from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        words = {word: i for i, word in enumerate(words)}

        for word, idx in words.items():
            N = len(word)

            for p in range(N + 1):
                prefix = word[:p]
                suffix = word[p:]

                if prefix == prefix[::-1]:
                    prepend_candidate = suffix[::-1]

                    if prepend_candidate in words and prepend_candidate != word:
                        res.append([words[prepend_candidate], idx])

                if suffix == suffix[::-1]:
                    append_candidate = prefix[::-1]

                    if p != N and append_candidate in words and append_candidate != word:
                        res.append([idx, words[append_candidate]])

        return res

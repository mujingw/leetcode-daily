from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        flags = [True] * len(words)
        N = len(words)
        words.sort(key=lambda x: len(x))

        for i in range(N):
            for j in range(i + 1, N):
                if words[i] == words[j][-len(words[i]):]:
                    flags[i] = False
                    break

        return sum(len(words[i]) + 1 for i in range(N) if flags[i])

import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wl = set(wordList)
        q = collections.deque([(beginWord, 1)])
        seen = set([beginWord])

        while q:
            curr, steps = q.popleft()

            if curr == endWord:
                return steps

            for i in range(len(curr)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = curr[:i] + c + curr[i + 1:]

                    if next_word in wl and next_word not in seen:
                        seen.add(next_word)
                        q.append((next_word, steps + 1))

        return 0

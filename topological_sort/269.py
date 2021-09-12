from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def add_vertices(w, g):
            for ch in w:
                if ch not in g:
                    g[ch] = set()

            return

        def add_words(g, w1, w2):
            add_vertices(w1, g)

            N = min(len(w1), len(w2))
            found = False

            for i in range(N):
                if w1[i] != w2[i]:
                    g[w1[i]].add(w2[i])
                    found = True
                    break

            if (not found) and len(w1) > len(w2):
                return False

            return True

        def build_graph(words):
            g = defaultdict(set)

            for w1, w2 in zip(words, words[1:]):
                if not add_words(g, w1, w2):
                    return defaultdict(set)

            add_vertices(words[-1], g)

            return g

        def dfs(curr, g, visited, visiting, q):
            visiting.add(curr)

            for neig in g[curr]:
                if neig in visiting:
                    return True

                if neig not in visited:
                    if dfs(neig, g, visited, visiting, q):
                        return True

            visiting.remove(curr)
            visited.add(curr)
            q.appendleft(curr)

            return False

        g = build_graph(words)
        visited, visiting, q = set(), set(), deque()

        for ch in list(g.keys()):
            if ch not in visited:
                if dfs(ch, g, visited, visiting, q):
                    return ""

        return "".join(q)

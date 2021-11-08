class TrieNode(object):
    def __init__(self, word):
        self.children = {}
        self.word = word


class PrefixTrieTable(object):
    def __init__(self, words):
        self.root = TrieNode(None)

        for w in words:
            self.add_to_trie(w)

    def add_to_trie(self, w):
        root = self.root

        for ch in w:
            if ch in root.children:
                root = root.children[ch]
            else:
                root.children[ch] = TrieNode(None)
                root = root.children[ch]

        root.word = w

    def collect(self, root, candidates):
        if root.word:
            candidates.append(root.word)
        else:
            for ch in root.children:
                self.collect(root.children[ch], candidates)

    def get_prefix_matches(self, prefix):
        candidates, root = [], self.root

        for ch in prefix:
            root = root.children[ch] if ch in root.children else None

            if not root:
                return candidates

        self.collect(root, candidates)

        return candidates


class Solution(object):
    def backtrack(self, res, so_far, N, words, table):
        if len(so_far) == N:
            res.append([x for x in so_far])
        else:
            prefix = ''.join([x[len(so_far)] for x in so_far])

            for c in table.get_prefix_matches(prefix):
                so_far.append(c)
                self.backtrack(res, so_far, N, words, table)
                so_far.pop()

    def wordSquares(self, words):
        res = []

        if words:
            table = PrefixTrieTable(words)
            self.backtrack(res, [], len(words[0]), words, table)

        return res

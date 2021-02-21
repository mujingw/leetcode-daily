class TrieNode:
    def __init__(self, val, is_word):
        self.is_word = is_word
        self.val = val
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode("", False)

    def add(self, word):
        i = 0
        curr = self.root

        while i < len(word):
            if word[i] not in curr.children:
                curr.children[word[i]] = TrieNode(word[i], False)

            curr = curr.children[word[i]]
            i += 1

        curr.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(res, curr, board, R, C, r, c, node, visited):
            if node.is_word:
                res.append("".join(curr))
                node.is_word = False

            if r < 0 or r >= R or c < 0 or c >= C:
                return

            if (r, c) in visited:
                return

            ch = board[r][c]
            node = node.children[ch] if ch in node.children else None

            if not node:
                return

            visited.add((r, c))
            curr.append(ch)
            dfs(res, curr, board, R, C, r + 1, c, node, visited)
            dfs(res, curr, board, R, C, r, c + 1, node, visited)
            dfs(res, curr, board, R, C, r - 1, c, node, visited)
            dfs(res, curr, board, R, C, r, c - 1, node, visited)
            curr.pop()
            visited.remove((r, c))

        trie = Trie()
        res = []
        R, C = len(board), len(board[0])

        for word in set(words):
            trie.add(word)

        for i in range(R):
            for j in range(C):
                dfs(res, [], board, R, C, i, j, trie.root, set())

        return res

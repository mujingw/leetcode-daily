class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            curr = curr.children[ch]

        curr.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(res, curr, board, R, C, r, c, node):
            if node.is_word:
                res.append("".join(curr))
                node.is_word = False

            if r < 0 or r >= R or c < 0 or c >= C:
                return

            ch = board[r][c]
            node = node.children[ch] if ch in node.children else None

            if not node:
                return

            curr.append(ch)
            board[r][c] = "#"
            dfs(res, curr, board, R, C, r + 1, c, node)
            dfs(res, curr, board, R, C, r, c + 1, node)
            dfs(res, curr, board, R, C, r - 1, c, node)
            dfs(res, curr, board, R, C, r, c - 1, node)
            board[r][c] = ch
            curr.pop()

        trie = Trie()
        res = []
        R, C = len(board), len(board[0])

        for word in set(words):
            trie.add(word)

        for i in range(R):
            for j in range(C):
                dfs(res, [], board, R, C, i, j, trie.root)

        return res

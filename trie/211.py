class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()

            curr = curr.children[ch]

        curr.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        """
        curr = self.root
        res = [False]
        self.dfs(res, curr, word)

        return res[0]

    def dfs(self, res, curr, word):
        if word == "":
            if curr.is_word:
                res[0] = True
            return

        ch = word[0]

        if ch == ".":
            for next_node in curr.children.values():
                self.dfs(res, next_node, word[1:])
        else:
            if ch in curr.children:
                self.dfs(res, curr.children[ch], word[1:])

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

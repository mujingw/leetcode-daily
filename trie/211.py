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
        return self.dfs(self.root, word)

    def dfs(self, curr, word):
        if word == "":
            return curr.is_word

        ch = word[0]

        if ch == ".":
            return any(self.dfs(nx_ch, word[1:]) for nx_ch in curr.children.values())
        else:
            if ch in curr.children:
                return self.dfs(curr.children[ch], word[1:])
            else:
                return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

from typing import List


class Node:
    def __init__(self):
        self.children = {}
        self.num = -1


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, s, num):
        curr = self.root

        for digit in s:
            if digit not in curr.children:
                curr.children[digit] = Node()

            curr = curr.children[digit]

        curr.num = num

    def find_max_xor(self, s, num):
        curr = self.root

        for digit in s:
            if digit == "0" and "1" in curr.children:
                curr = curr.children["1"]
            elif digit == "1" and "0" in curr.children:
                curr = curr.children["0"]
            else:
                curr = curr.children[digit]

        return num ^ curr.num


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        trie = Trie()
        lookup = {}

        for num in nums:
            bin_rep = bin(num)[2:].zfill(32)
            lookup[num] = bin_rep
            trie.add(bin_rep, num)

        for num in nums:
            res = max(res, trie.find_max_xor(lookup[num], num))

        return res

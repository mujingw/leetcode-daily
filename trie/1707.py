class Node:
    def __init__(self):
        self.children = {}
        self.val = -1


class Trie:
    def __init__(self):
        self.root = Node()

    def empty(self):
        return len(self.root.children) == 0

    def add(self, s, num):
        curr = self.root

        for digit in s:
            if digit not in curr.children:
                curr.children[digit] = Node()

            curr = curr.children[digit]

        curr.val = num

    def find_max_xor(self, s, num):
        curr = self.root

        for digit in s:
            if digit == "0" and "1" in curr.children:
                curr = curr.children["1"]
            elif digit == "1" and "0" in curr.children:
                curr = curr.children["0"]
            else:
                curr = curr.children[digit]

        return num ^ curr.val


class Solution:
    def num_to_bin(self, num):
        return bin(num)[2:].zfill(32)

    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        trie = Trie()
        nums.sort()
        queries_sorted_by_limit = sorted([(limit, num, i) for i, (num, limit) in enumerate(queries)])
        p = 0

        for limit, val, i in queries_sorted_by_limit:
            while p < len(nums) and nums[p] <= limit:
                trie.add(self.num_to_bin(nums[p]), nums[p])
                p += 1

            if not trie.empty():
                res[i] = trie.find_max_xor(self.num_to_bin(val), val)

        return res

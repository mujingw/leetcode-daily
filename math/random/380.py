from random import randrange


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val2idx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val2idx:
            return False

        self.nums.append(val)
        self.val2idx[val] = len(self.nums) - 1

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.val2idx:
            return False

        last_val = self.nums[-1]
        idx = self.val2idx[val]

        self.nums[idx] = last_val
        self.nums.pop()

        self.val2idx[last_val] = idx
        del self.val2idx[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[randrange(0, len(self.nums))]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

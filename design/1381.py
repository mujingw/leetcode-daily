class CustomStack:

    def __init__(self, max_size: int):
        self.capacity = max_size
        self.storage = []

    def push(self, x: int) -> None:
        if len(self.storage) < self.capacity:
            self.storage.append(x)

    def pop(self) -> int:
        if self.storage:
            return self.storage.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        boundary = min(k, len(self.storage))

        for i in range(boundary):
            self.storage[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)

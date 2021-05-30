class ProductOfNumbers:
    def __init__(self):
        self.pre_product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.pre_product = [1]
        else:
            last = self.pre_product[-1]
            self.pre_product.append(last * num)

    def getProduct(self, k: int) -> int:
        if k < len(self.pre_product):
            return self.pre_product[-1] // self.pre_product[-k-1]
        else:
            return 0


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

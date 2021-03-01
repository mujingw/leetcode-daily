class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        count = 1

        if not self.s:
            self.s.append((price, count))
        else:
            while self.s and self.s[-1][0] <= price:
                count += self.s.pop()[1]

            self.s.append((price, count))

        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
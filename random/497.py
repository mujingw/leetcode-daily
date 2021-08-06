from random import randint


class Solution(object):

    def __init__(self, rects):
        self.rects = rects
        self.presum = []
        self._sum = 0

        for x1, y1, x2, y2 in self.rects:
            area = (y2 - y1 + 1) * (x2 - x1 + 1)
            self._sum += area
            self.presum.append(self._sum)

    def pick(self):
        val = randint(0, self._sum - 1)
        left, right = 0, len(self.presum) - 1

        while left < right:
            mid = left + (right - left) // 2
            if self.presum[mid] > val:
                right = mid
            else:
                left = mid + 1

        x1, y1, x2, y2 = self.rects[left]
        height, width = y2 - y1 + 1, x2 - x1 + 1
        base = self.presum[left] - height * width
        x = x1 + (val - base) % width
        y = y1 + (val - base) // width

        return x, y

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

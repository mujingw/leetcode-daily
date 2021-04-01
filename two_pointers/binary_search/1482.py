from typing import List


class Solution:
    def minDays(self, bloom_day: List[int], m: int, k: int) -> int:
        def ok(day):
            adjacent_flowers = 0
            bouquet_made = 0

            for d in bloom_day:
                if d <= day:
                    adjacent_flowers += 1

                    if adjacent_flowers == k:
                        adjacent_flowers = 0
                        bouquet_made += 1

                    if bouquet_made == m:
                        return True
                else:
                    adjacent_flowers = 0

            return False

        l, r = 1, 10 ** 9 + 1

        while l < r:
            mid = (l + r) // 2

            if ok(mid):
                r = mid
            else:
                l = mid + 1

        return l if ok(l) else -1

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s = []
        s3 = float("inf")

        for num in nums[::-1]:
            if not s:
                s.append(num)
            else:
                if s3 != float("inf") and num < s3:
                    return True

                while s and num > s[-1]:
                    s3 = s.pop()

                s.append(num)

        return False

from functools import reduce
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor2 = reduce(lambda x, y: x ^ y, nums)
        mask = xor2 & -xor2
        res = [0, 0]

        for num in nums:
            if num & mask == 0:
                res[0] ^= num
            else:
                res[1] ^= num

        return res

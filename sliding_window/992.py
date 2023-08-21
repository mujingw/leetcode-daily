from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def at_most(A, k):
            res = 0
            window = defaultdict(int)
            left, right = 0, 0

            while right < len(A):
                num = A[right]
                right += 1
                window[num] += 1

                while len(window) > k:
                    num = A[left]
                    left += 1
                    window[num] -= 1

                    if window[num] == 0:
                        del window[num]

                res += (right - left + 1)

            return res

        return at_most(A, K) - at_most(A, K - 1)

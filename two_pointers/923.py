from collections import Counter
from math import comb
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr)
        arr.sort()
        MOD, N, res = 10 ** 9 + 7, len(arr), 0

        for i in range(N - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            l, r = i + 1, N - 1

            while l < r:
                a, b, c = arr[i], arr[l], arr[r]
                s = a + b + c

                if s == target:
                    if a == b == c:
                        res += comb(counter[a], 3)
                    elif a == b:
                        res += (comb(counter[a], 2) * counter[c])
                    elif b == c:
                        res += (comb(counter[b], 2) * counter[a])
                    else:
                        res += (counter[a] * counter[b] * counter[c])

                    l += 1

                    while l < r and arr[l] == arr[l - 1]:
                        l += 1

                    r -= 1

                    while l < r and arr[r] == arr[r + 1]:
                        r -= 1

                elif s < target:
                    l += 1
                else:
                    r -= 1

        return res % MOD

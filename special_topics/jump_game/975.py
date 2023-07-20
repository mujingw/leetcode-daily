from typing import List

from sortedcontainers import SortedDict


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        N = len(arr)
        odd = [False] * N
        even = [False] * N
        odd[-1] = True
        even[-1] = True
        sd = SortedDict()
        sd[arr[N - 1]] = N - 1

        for i in range(N - 2, -1, -1):
            if arr[i] in sd:
                odd[i] = even[sd[arr[i]]]
                even[i] = odd[sd[arr[i]]]
            else:
                # greatest smaller
                floor_idx = sd.bisect_left(arr[i]) - 1

                if floor_idx != -1:
                    even[i] = odd[sd.peekitem(floor_idx)[1]]

                # smallest greater
                ceiling_idx = sd.bisect_left(arr[i])

                if ceiling_idx != len(sd):
                    odd[i] = even[sd.peekitem(ceiling_idx)[1]]

            sd[arr[i]] = i

        return odd.count(True)

from collections import deque


class Solution(object):
    def maxResult(self, nums, k):
        scores = [float("-inf")] * len(nums)
        scores[0] = nums[0]
        mono_q = deque([0])

        for i, num in enumerate(nums[1:], 1):
            while mono_q and mono_q[0] < i - k:
                mono_q.popleft()

            scores[i] = scores[mono_q[0]] + num

            while mono_q and scores[mono_q[-1]] < scores[i]:
                mono_q.pop()

            mono_q.append(i)

        return scores[-1]

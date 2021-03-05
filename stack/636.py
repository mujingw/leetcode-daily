from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = [int(logs[0].split(":")[0])]
        prev = int(logs[0].split(":")[2])

        for log in logs[1:]:
            curr_job = log.split(":")
            i, action, time = int(curr_job[0]), curr_job[1], int(curr_job[2])

            if action == "start":
                if stack:
                    res[stack[-1]] += time - prev

                stack.append(i)
                prev = time
            else:
                res[stack[-1]] += time - prev + 1
                stack.pop()
                prev = time + 1

        return res

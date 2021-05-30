from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        bad_chars = [ch for ch, count in Counter(s).items() if count < k]

        if bad_chars:
            best = 0

            for sub_string in s.split(bad_chars[0]):
                if len(sub_string) >= k:
                    best = max(best, self.longestSubstring(sub_string, k))

            return best
        else:
            return len(s)

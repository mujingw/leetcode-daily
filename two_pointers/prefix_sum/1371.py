class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a": 16, "e": 8, "i": 4, "o": 2, "u": 1}
        pre, res, vowels_xor = {0: -1}, 0, 0

        for i, ch in enumerate(s):
            if ch in vowels:
                vowels_xor ^= vowels[ch]

            if vowels_xor not in pre:
                pre[vowels_xor] = i

            res = max(res, i - pre[vowels_xor])

        return res

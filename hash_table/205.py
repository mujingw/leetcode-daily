class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s, t):
            d = {}

            for a, b in zip(s, t):
                if a not in d:
                    d[a] = b
                else:
                    if d[a] != b:
                        return False

            return True

        return helper(s, t) and helper(t, s)

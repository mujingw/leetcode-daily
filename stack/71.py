class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []

        for d in path.split("/"):
            if d == "." or d == "":
                continue
            elif d == "..":
                if s:
                    s.pop()
            else:
                s.append(d)

        return "/" + "/".join(s)

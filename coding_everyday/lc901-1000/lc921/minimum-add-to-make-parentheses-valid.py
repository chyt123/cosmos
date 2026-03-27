class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l = []
        for c in s:
            if c == ')' and len(l)>0 and l[-1]=='(':
                l.pop()
            else:
                l.append(c)
        return len(l)
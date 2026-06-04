class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        check = [i for i in range(26)]
        def idx(a: str) -> int:
            return ord(a) - ord('a')
        
        def root(i: int) -> int:
            nonlocal check
            while check[i] != i:
                i = check[i]
            return i


        m = len(s1)
        n = len(baseStr)

        for i in range(m):
            i1 = root(idx(s1[i]))
            i2 = root(idx(s2[i]))
            if i1 < i2:
                check[i2] = i1
            else:
                check[i1] = i2
        
        ans = ''
        for i in range(n):
            # find eq baseStr[i]
            eqi = idx(baseStr[i])
            ans += chr(ord('a') + root(eqi))

        return ans

# []
# l=p
# e=r=c=o=a=s
# t=g
# d=m




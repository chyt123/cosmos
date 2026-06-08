class Solution:
    def smallestSubsequence(self, s: str) -> str:
        def idx(c):
            return ord(c) - ord('a')
    
        last_occ = [-1] * 26
        for i, c in enumerate(s):
            last_occ[idx(c)] = max(last_occ[idx(c)], i)
        
        # print(last_occ)

        ans = []
        v = set()
        for i, c in enumerate(s):
            # print(c, v, ans)
            if c in v:
                continue
            if not ans or ord(c) > ord(ans[-1]):
                v.add(c)
                ans.append(c)
                continue
            if ord(c) == ord(ans[-1]):
                continue

            while ans and ord(c) < ord(ans[-1]) and last_occ[idx(ans[-1])] > i:
                p = ans.pop()
                v.remove(p)
            v.add(c)
            ans.append(c)

        return ''.join(ans)
# cbacdcbc
# acdb

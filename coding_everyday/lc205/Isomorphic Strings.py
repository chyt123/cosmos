import bisect
import collections
from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds, dt = dict(), dict()
        fmts, fmtt = '', ''
        cnts, cntt = 0, 0
        for i in range(len(s)):
            if s[i] not in ds:
                ds[s[i]] = cnts
                cnts += 1
            if t[i] not in dt:
                dt[t[i]] = cntt
                cntt += 1
            fmts += str(ds[s[i]])
            fmtt += str(dt[t[i]])
        return fmts == fmtt


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["egg", "add"],
        ["foo", "bar"],
        ["paper", "title"],
    ]
    for i, j in test_cases:
        print(sol.isIsomorphic(i, j))

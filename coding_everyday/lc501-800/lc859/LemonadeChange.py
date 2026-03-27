import bisect
import collections
import math
import re
from typing import List


class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        if len(a) != len(b):
            return False
        diff = []
        for i in range(len(a)):
            if a[i] != b[i]:
                diff.append([a[i], b[i]])
        if len(diff) == 0:
            seen = set()
            for i in a:
                if i in seen:
                    return True
                seen.add(i)
            return False
        if len(diff) == 2:
            diff[0].reverse()
            return diff[0] == diff[1]


if __name__ == "__main__":
    a = "aaaaabc"
    b = "aaaaacb"
    sol = Solution()
    print(sol.buddyStrings(a, b))
import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        return len(l[-1]) if l else 0


if __name__ == "__main__":
    sol = Solution()
    s = "Hello World"
    s = ' '
    print(sol.lengthOfLastWord(s))

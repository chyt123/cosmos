import bisect
import math
import re
from typing import List


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        l = len(s)
        q = []
        for i in range(l):
            if s[i] == '(':
                q.append(0)
            elif s[i] == ')':
                if q[-1] == 0:
                    q[-1] = 1
                else:
                    suum = 0
                    idx = len(q) - 1
                    while q[idx] != 0:
                        suum += q[idx]
                        q.pop()
                        idx -= 1
                    q[idx] = 2 * suum
        return sum(q)


if __name__ == "__main__":
    s = "()()"
    s = "(()(()))"
    s = "((()))"
    sol = Solution()
    print(sol.scoreOfParentheses(s))
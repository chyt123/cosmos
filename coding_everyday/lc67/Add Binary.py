import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la, lb = len(a), len(b)
        if la > lb:
            b = '0' * (la - lb) + b
        else:
            a = '0' * (lb - la) + a
        pt = len(a) - 1
        rst = ''
        plus = 0
        while pt >= 0:
            add = int(a[pt]) + int(b[pt]) + plus
            rst += str(add % 2)
            plus = int(add) // 2
            pt -= 1
        if plus:
            rst += '1'
        return rst[::-1]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["1010", "1011"],
        ["11", "1"],
    ]
    for i, j in test_cases:
        print(sol.addBinary(i, j))

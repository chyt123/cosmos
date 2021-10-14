from typing import List
from collections import defaultdict


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 3:
            return 1
        l, r = 0, x - 1
        while l < r - 1:
            m = (l + r) // 2
            if m ** 2 > x:
                r = m
            elif m ** 2 < x:
                l = m + 1
            else:
                return m

        return l if l ** 2 <= x else l - 1


if __name__ == "__main__":
    sol = Solution()
    x = 8
    for i in range(0, 26):
        print(i, sol.mySqrt(i))

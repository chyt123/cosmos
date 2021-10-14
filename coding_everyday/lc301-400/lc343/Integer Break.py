import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        mem = [0 for _ in range(n + 1)]
        mem[2] = 1
        mem[3] = 2

        def helper(num):
            print(num)
            if num < 5:
                return num
            if mem[num] > 0:
                return mem[num]
            maxx = 0
            for i in range(2, num // 2 + 1):
                maxx = max(maxx, helper(i) * helper(num - i))
                mem[num] = maxx
            return mem[num]

        return helper(n)


if __name__ == "__main__":
    sol = Solution()
    n = 8
    print(sol.integerBreak(n))

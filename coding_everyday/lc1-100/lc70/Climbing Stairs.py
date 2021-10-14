import collections
import math
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        a1 = 1
        a2 = 1
        if n < 2:
            return 1
        suum = 0
        for i in range(2, n + 1):
            suum = a1 + a2
            a1 = a2
            a2 = suum
        return suum


if __name__ == "__main__":
    sol = Solution()
    n = 2
    print(sol.climbStairs(n))



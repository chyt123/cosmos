import math
from typing import List
from collections import deque, defaultdict


class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)


if __name__ == "__main__":
    sol = Solution()
    for n in range(0, 26):
        print(sol.trailingZeroes(n))

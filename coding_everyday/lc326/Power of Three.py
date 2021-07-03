import math
from typing import List
from collections import deque, defaultdict


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 20 % n == 0


if __name__ == "__main__":
    sol = Solution()
    n = 129140162
    print(sol.isPowerOfThree(n))
    # for n in range(0, 28):
    #     print(sol.isPowerOfThree(n))

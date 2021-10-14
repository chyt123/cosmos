import collections
import math
from typing import List


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, math.floor(math.sqrt(c))
        while l <= r:
            if l ** 2 + r ** 2 > c:
                r -= 1
            elif l ** 2 + r ** 2 < c:
                l += 1
            else:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    c = 1
    print(sol.judgeSquareSum(c))



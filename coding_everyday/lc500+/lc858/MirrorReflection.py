import bisect
import math
import re
from typing import List


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        lcm = p * q // math.gcd(p, q)
        # a * p == b * q
        a, b = lcm / p, lcm / q

        if b % 2 == 0:
            return 2
        else:
            return 0 if a % 2 == 0 else 1


if __name__ == "__main__":
    p = 6
    q = 5
    p = 2
    q = 1
    sol = Solution()
    print(sol.mirrorReflection(p, q))
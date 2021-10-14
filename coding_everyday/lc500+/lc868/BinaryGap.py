import math
from typing import List
from collections import deque, defaultdict


class Solution:
    def binaryGap(self, n: int) -> int:
        cnt = 0
        pre = math.inf
        first = True
        maax = 0
        while n > 0:
            r = n % 2
            n = n // 2
            cnt += 1
            if r == 1:
                if first:
                    pre = cnt
                    first = False
                    continue
                maax = max(maax, cnt - pre)
                pre = cnt
        return maax


if __name__ == "__main__":
    sol = Solution()
    n = 5
    n = 22
    n = 1
    print(sol.binaryGap(n))

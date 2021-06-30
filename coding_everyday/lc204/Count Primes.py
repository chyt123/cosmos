import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        cnt = n
        prime = [True for _ in range(n + 1)]
        cnt -= 2
        for i in range(2, n // 2 + 1):
            if prime[i]:
                for j in range(2 * i, n, i):
                    if prime[j]:
                        prime[j] = False
                        cnt -= 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    n = 10
    print(sol.countPrimes(n))

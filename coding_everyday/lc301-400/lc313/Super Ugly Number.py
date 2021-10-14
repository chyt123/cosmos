import math
from typing import List
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        cand = [(p, p, 1) for p in primes]
        ugly = [1]
        for _ in range(n - 1):
            ugly.append(cand[0][0])
            while cand[0][0] == ugly[-1]:
                x, p, i = heapq.heappop(cand)
                heapq.heappush(cand, (p * ugly[i], p, i + 1))
        return ugly[-1]


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [12, [2, 7, 13, 19]]
    ]
    for i, j in test_cases:
        print(sol.nthSuperUglyNumber(i, j))
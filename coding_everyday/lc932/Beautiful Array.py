import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        mem = defaultdict()
        mem[1] = [1]

        def cal(num):
            if num in mem:
                return mem[num]
            odds = cal((num + 1) // 2)
            evens = cal(num // 2)
            mem[num] = [2 * x - 1 for x in odds] + [2 * x for x in evens]
            return mem[num]
        return cal(n)


if __name__ == "__main__":
    sol = Solution()
    n = 7
    print(sol.beautifulArray(n))

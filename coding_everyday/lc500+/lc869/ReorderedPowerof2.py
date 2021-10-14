import math
from typing import List
from collections import deque, defaultdict


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sto = defaultdict(list)
        for i in range(30):
            tmp = [i for i in str(2 ** i)]
            tmp.sort()
            sto[len(tmp)].append(tmp)
        ln = [i for i in str(n)]
        ln.sort()
        l = len(ln)
        for i in sto[l]:
            if ln == i:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    n = 46
    print(sol.reorderedPowerOf2(n))

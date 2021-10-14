import math
from typing import List


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        if target <= 1:
            return target
        for i in range(1, target):
            sum = i * (i + 1) / 2
            if sum >= target:
                break

        while (sum - target) % 2 != 0:
            i += 1
            sum = i * (i + 1) / 2

        return i


if __name__ == "__main__":
    sol = Solution()
    target = 0
    print(sol.reachNumber(target))

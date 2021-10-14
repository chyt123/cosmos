import bisect
import collections
import math
import re
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10:
                if fives >= 1:
                    fives -= 1
                    tens += 1
                else:
                    return False
            elif i == 20:
                if tens >= 1 and fives >= 1:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True


if __name__ == "__main__":
    sol = Solution()
    bills = [5, 5, 5, 10, 20]
    bills = [10,10]
    bills = [5, 5, 10, 10, 20]
    print(sol.lemonadeChange(bills))
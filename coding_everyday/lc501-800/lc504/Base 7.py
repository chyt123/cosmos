import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def convertToBase7(self, num: int) -> str:
        neg = False if num >= 0 else True
        num = abs(num)
        ans = ''
        while num >= 7:
            ans += str(num % 7)
            num //= 7
        ans += str(num)
        if neg:
            ans += '-'
        return ans[::-1]


if __name__ == "__main__":
    sol = Solution()
    num = -7
    print(sol.convertToBase7(num))

import bisect
import collections
import copy
import math
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pt = len(digits) - 1
        plus = 0
        while plus and pt >= 0 or pt == len(digits) - 1:
            digits[pt] += 1
            if digits[pt] == 10:
                digits[pt] = 0
                plus = 1
            else:
                plus = 0
            pt -= 1
        return [1] + digits if plus == 1 else digits


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 9, 8],
        [3, 9, 9],
        [3, 2],
        [9, 9, 9],
    ]
    for i in test_cases:
        print(sol.plusOne(i))

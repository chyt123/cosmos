import bisect
import math
from typing import List
from collections import defaultdict


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        mem = defaultdict()

        def cal(start, end):
            if (start, end) in mem:
                return mem[(start, end)]
            ways = []
            for i in range(start, end):
                if expression[i] in ['+', '-', '*']:
                    left = cal(start, i)
                    right = cal(i + 1, end)
                    for l in left:
                        for r in right:
                            if expression[i] == '+':
                                ways.append(l + r)
                            elif expression[i] == '-':
                                ways.append(l - r)
                            elif expression[i] == '*':
                                ways.append(l * r)
            if not ways:
                ways.append(int(expression[start:end]))
            mem[(start, end)] = ways
            return ways
        return cal(0, len(expression))


if __name__ == "__main__":
    sol = Solution()
    expression = "2*3-4*5"
    expression = '11'
    print(sol.diffWaysToCompute(expression))

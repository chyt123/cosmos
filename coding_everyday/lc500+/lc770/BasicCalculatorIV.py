import re
from collections import Counter
from typing import List


class Poly(Counter):
    def __add__(self, other):
        self.update(other)
        return self

    def __sub__(self, other):
        self.subtract(other)
        return self

    def __mul__(self, other):
        ans = Poly()
        for k, v in self.items():
            for k1, v1 in other.items():
                ans[tuple(sorted(k + k1))] += v * v1
        return Poly(ans)


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        val = dict(zip(evalvars, evalints))

        def f(s: str):
            s = val.get(s, s)
            return Poly({(s,): 1}) if isinstance(s, str) and s.isalpha() else Poly({(): int(s)})

        poly = eval(re.sub('(\w+)', r'f("\1")', expression))
        ans = []
        for k in sorted(poly.keys(), key=lambda item: (-len(item), item)):
            i = str(poly[k])
            if i == '0':
                continue
            elif k:
                i += '*' + '*'.join(k)
            ans.append(i)
        return ans



if __name__ == "__main__":
    sol = Solution()
    expression = "e + 8 - a + 5"
    evalvars = ["e"]
    evalints = [1]
    expression = "a * b * c + b * a * c * 4"
    evalvars = []
    evalints = []
    expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))"
    evalvars = []
    evalints = []
    expression = "e - 8 + temperature - pressure"
    evalvars = ["e", "temperature"]
    evalints = [1, 12]
    expression = "(e + 8) * (e - 8)"
    evalvars = []
    evalints = []
    print(sol.basicCalculatorIV(expression, evalvars, evalints))

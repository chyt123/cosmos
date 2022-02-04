import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        mem = dict()
        neg = False

        # negative num
        if numerator / denominator < 0:
            neg = True
            numerator = abs(numerator)
            denominator = abs(denominator)

        # before dot
        quo = numerator // denominator
        rem = numerator % denominator
        rtn = str(quo)
        if rem == 0:
            return '-' + rtn if neg else rtn
        rtn += '.'

        # after dot
        idx = 0
        frac = []
        while 1:
            num = rem * 10
            quo = num // denominator
            rem = num % denominator
            if rem == 0:
                frac.append(str(quo))
                break
            elif (quo, rem) not in mem:
                mem[quo, rem] = idx
                frac.append(str(quo))
            else:
                frac.insert(mem[quo, rem], '(')
                frac.append(')')
                break
            idx += 1
        rtn += ''.join(frac)
        return '-' + rtn if neg else rtn


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2],
        [2, 1],
        [4, 333],
        [2, 7],
        [1, 6],
        [-50, 8],
        [-2147483648, 1]
    ]
    for i in test_cases:
        result = sol.fractionToDecimal(i[0], i[1])
        print(result)

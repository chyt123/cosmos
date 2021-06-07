import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict
from util import (
    TreeNode, lc_list2tree,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stru = []
        start = 0
        words = ['']
        for idx, i in enumerate(s):
            if i.isnumeric():
                m = stru[-1][0] * stru[-1][1] if stru else 0
                stru.append([idx - start + m, int(i)])
                words.append('')
                start = idx + 1
            else:
                words[-1] += i
        while stru and k <= stru[-1][0] * stru[-1][1]:
            k = k - (math.ceil(k / stru[-1][0]) - 1)* stru[-1][0]
            stru.pop()
            words.pop()
        # print(stru, words)
        # print(k)
        bias = stru[-1][0] * stru[-1][1] if stru else 0
        return words[-1][k - bias - 1]


if __name__ == "__main__":
    sol = Solution()
    s = "leet2code3abcd2cde"
    k = 10
    s = "ha22"
    k = 5
    s = "a2345678999999999999999"
    k = 1
    print(sol.decodeAtIndex(s, k))

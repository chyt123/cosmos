import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        l1 = len(v1)
        l2 = len(v2)
        n = min(l1, l2)

        if l1 > l2:
            v_extra = v1
            rtn = 1
        else:
            v_extra = v2
            rtn = -1

        for i in range(0, n):
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1
        for i in range(n, max(l1, l2)):
            if int(v_extra[i]) > 0:
                return rtn
        return 0


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["1.01", "1.001"],
        ["1.0", "1.0.0"],
        ["0.1", "1.1"]
    ]
    for i in test_cases:
        result = sol.compareVersion(i[0], i[1])
        print(result)

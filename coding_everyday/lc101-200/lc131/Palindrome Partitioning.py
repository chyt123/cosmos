import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def is_palind(s):
            l = len(s)
            for i in range(0, l // 2 + 1):
                if s[i] != s[l - i - 1]:
                    return False
            return True

        def bt(cur_s, cur_l):
            if not cur_s:
                ans.append(cur_l[:])
            for i in range(1, len(cur_s) + 1):
                if is_palind(cur_s[:i]):
                    cur_l.append(cur_s[:i])
                    bt(cur_s[i:], cur_l)
                    cur_l.pop()

        bt(s, [])
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "aab",
        "a",
        "caabaac"
    ]
    for i in test_cases:
        print(sol.partition(i))

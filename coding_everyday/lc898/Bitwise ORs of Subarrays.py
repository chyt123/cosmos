import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        for i in arr:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [0],
        [1, 1, 2],
        [1, 2, 4]
    ]
    for i in test_cases:
        print(sol.subarrayBitwiseORs(i))


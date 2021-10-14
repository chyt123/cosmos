import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        mem = {
            1: [TreeNode()]
        }

        def helper(k):
            if k not in mem:
                rtn = []
                for i in range(1, k - 1, 2):
                    for left in helper(i):
                        for right in helper(k - i - 1):
                            cur = TreeNode()
                            cur.left = left
                            cur.right = right
                            rtn.append(cur)
                mem[k] = rtn
            return mem[k]

        return helper(n)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        7,
        3,
    ]
    for i in test_cases:
        result = (sol.allPossibleFBT(i))
        for j in result:
            print(lc_tree2list(j))


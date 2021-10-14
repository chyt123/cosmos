import bisect
from copy import deepcopy
from typing import List, Optional
from collections import defaultdict
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check_node(n1, n2):
            if n1 and n2 and n1.val == n2.val or not n1 and not n2:
                if not n1 and not n2 or not n1.left and not n1.right and not n2.left and not n2.right:
                    return True
                return check_node(n1.left, n2.left) and check_node(n1.right, n2.right)
            return False
        return check_node(p, q)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1,2,3], [1,2,3]],
        [[1, 2], [1, None, 2]],
        [[1,2,1], [1,1,2]],
        [[], []]
    ]
    for i, j in test_cases:
        result = sol.isSameTree(lc_list2tree(i), lc_list2tree(j))
        print(result)

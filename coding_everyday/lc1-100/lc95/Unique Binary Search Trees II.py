import bisect
from copy import deepcopy
from typing import List
from collections import defaultdict
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def build_tree(start, end):
            if start > end:
                return [None]
            rtn = []
            for cur_val in range(start, end + 1):
                cur_left = build_tree(start, cur_val - 1)
                cur_right = build_tree(cur_val + 1, end)
                for left in cur_left:
                    for right in cur_right:
                        node = TreeNode(cur_val)
                        node.left = left
                        node.right = right
                        rtn.append(node)
            return rtn

        if n == 0:
            return [None]
        return build_tree(1, n)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        2,3
    ]
    for i in test_cases:
        result = sol.generateTrees(i)
        print('hhh')
        for t in result:
            print(lc_tree2list(t))

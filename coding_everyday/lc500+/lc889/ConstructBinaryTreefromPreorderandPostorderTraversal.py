import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict, Counter
from util import (
    TreeNode, lc_list2tree, lc_tree2list,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(pre_tran, post_tran):
            if not pre_tran:
                return None
            ret = TreeNode(pre_tran[0])
            if len(pre_tran) > 1:
                right_root = post_tran[-2]
                right_idx = pre_tran.index(right_root)
                ret.left = helper(pre_tran[1:right_idx], post_tran[:right_idx - 1])
                ret.right = helper(pre_tran[right_idx:], post_tran[right_idx - 1: len(post_tran) - 1])
            return ret

        ans = helper(pre, post)
        return ans


if __name__ == "__main__":
    sol = Solution()
    pre = [1, 2, 4, 5, 3, 6, 7]
    post = [4, 5, 2, 6, 7, 3, 1]
    tree = sol.constructFromPrePost(pre, post)
    print(lc_tree2list(tree))
import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pt = head
        pre = dict()
        cnt = 1
        while pt.next:
            pre[pt.next] = pt
            pt = pt.next
            cnt += 1
        # now pt is the last node
        # print(cnt)
        pt2 = head
        cnt = (cnt + 1) // 2
        while cnt > 1:
            pt.next = pt2.next
            pt2.next = pt
            pt2 = pt.next
            pt = pre[pt]
            cnt -= 1
        pt.next = None
        print(lc_singlelinkedlist2list(head))


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5]
    ]
    for i in test_cases:
        sol.reorderList(lc_list2singlelinkedlist(i))

import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001)
        dummy.next = to_insert = head
        while head and head.next:
            if head.val > head.next.val:
                to_insert = head.next
                pre = dummy
                while pre.next.val < to_insert.val:
                    pre = pre.next
                head.next = to_insert.next
                to_insert.next = pre.next
                pre.next = to_insert
            else:
                head = head.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [4,2,1,3],
        [-1,5,3,4,0],
    ]
    for i in test_cases:
        dummyult = sol.insertionSortList(lc_list2singlelinkedlist(i))
        print(lc_singlelinkedlist2list(dummyult))

import bisect
import math
from typing import List
from collections import deque, defaultdict, OrderedDict
from util import (
    TreeNode, lc_list2tree,
    ListNode, lc_list2singlelinkedlist
)


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        l = []
        while head:
            l.append(head)
            head = head.next
        return l[len(l) // 2]


if __name__ == "__main__":
    sol = Solution()
    l = [1,2,3,4,5,6]
    l = [1,2,3,4,5]
    l = lc_list2singlelinkedlist(l)
    print(sol.middleNode(l))

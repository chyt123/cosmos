import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    # test_cases = [
    #     [2,2,3,2],
    #     [0,1,0,1,0,1,99]
    # ]
    # for i in test_cases:
    #     print(sol.singleNumber(i))

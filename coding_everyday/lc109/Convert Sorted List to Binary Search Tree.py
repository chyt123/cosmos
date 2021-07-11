import collections
import math
from typing import List
from collections import defaultdict
from util import lc_list2tree, TreeNode, lc_tree2list, lc_list2singlelinkedlist, ListNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        slow, fast = head, head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:
            pre.next = None
        rtn = TreeNode(slow.val)
        rtn.left = self.sortedListToBST(head) if head != slow else None
        rtn.right = self.sortedListToBST(slow.next)
        return rtn


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [-10, -3, 0, 5, 9, 12],
        [-10, -3, 0, 5, 9],
    ]
    for i in test_cases:
        result = sol.sortedListToBST(lc_list2singlelinkedlist(i))
        print(lc_tree2list(result))



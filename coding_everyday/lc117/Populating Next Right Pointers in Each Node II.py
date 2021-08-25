import collections
from typing import List, Optional
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        pt = dummy = Node()
        while node:
            pt.next = node.left
            if pt.next:
                pt = pt.next
            pt.next = node.right
            if pt.next:
                pt = pt.next
            if node.next:
                node = node.next
            else:
                node = dummy.next
                pt = dummy
        return root



if __name__ == "__main__":
    sol = Solution()
    # test_cases = [
    #     [1, 2, 3, 4, 5, 6, 7],
    # ]
    # for i in test_cases:
    #     sol.connect(lc_list2tree(i))


import collections
import math
from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        sp = ListNode()
        sp.next = head
        pt = head
        pre = sp
        while pt and pt.next:
            if pt.val == pt.next.val:
                while pt.next and pt.val == pt.next.val:
                    pt.next = pt.next.next
                pre.next = pt.next
                pt = pre.next
            else:
                pre = pt
                pt = pt.next
        return sp.next


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [],
        [1, 2, 3, 3, 4, 4, 5],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
        [1, 1, 1, 2, 3],
    ]
    for i in test_cases:
        result = sol.deleteDuplicates(lc_list2singlelinkedlist(i))
        print(lc_singlelinkedlist2list(result))



import collections
import math
from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        s_pt = s_cur = ListNode()
        l_pt = l_cur = ListNode()
        while head:
            tmp = head.next
            if head.val < x:
                s_cur.next = head
                s_cur = s_cur.next
            else:
                l_cur.next = head
                l_cur = l_cur.next
            head.next = None
            head = tmp
        s_cur.next = l_pt.next
        return s_pt.next


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1, 4, 3, 2, 5, 2], 3],
        [[1, 4, 3, 2, 5, 2], 4],
    ]
    for i, j in test_cases:
        result = sol.partition(lc_list2singlelinkedlist(i), j)
        print(lc_singlelinkedlist2list(result))



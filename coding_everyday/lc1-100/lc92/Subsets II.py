import bisect
from typing import List
from collections import defaultdict
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        rtn = ListNode()
        rtn.next = head
        start = rtn
        cnt = 1
        while head and cnt != left:
            start = head
            head = head.next
            cnt += 1

        pre = None
        while head and cnt != right:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
            cnt += 1

        if head:
            start.next.next = head.next
            head.next = pre
            start.next = head

        return rtn.next


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[3, 5], 1, 1],
        [[1, 2, 3, 4, 5], 2, 4],
        [[5], 1, 1],
    ]
    for i, j, k in test_cases:
        result = sol.reverseBetween(lc_list2singlelinkedlist(i), j, k)
        print(lc_singlelinkedlist2list(result))

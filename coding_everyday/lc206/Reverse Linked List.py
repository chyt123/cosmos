import bisect
import collections
from typing import List
from util import lc_list2singlelinkedlist, ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        pre, cur = head, head.next
        head.next = None
        while cur:
            nxt = cur.next
            cur.next = pre
            cur, pre = nxt, cur
        return pre


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2],
        []
    ]
    for i in test_cases:
        head = lc_list2singlelinkedlist(i)
        rst = sol.reverseList(head)
        print(rst)

from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = ListNode()
        rtn = cur
        while head and head.next:
            new_head = head.next.next
            cur.next = head.next
            head.next.next = head
            head.next = None
            cur = head
            head = new_head
        if head:
            cur.next = head
        return rtn.next


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [],
        [1],
    ]
    for i in test_cases:
        i = lc_list2singlelinkedlist(i)
        result = sol.swapPairs(i)
        print(lc_singlelinkedlist2list(result))

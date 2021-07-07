from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        rtn = head
        while head:
            if head.next and head.val == head.next.val:
                nxt = head.next
                head.next = head.next.next
                del nxt
            else:
                head = head.next
        return rtn


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 1, 2, 3, 3],
        [1, 1, 1, 2, 2, 3],
    ]
    for i in test_cases:
        i = lc_list2singlelinkedlist(i)
        result = sol.deleteDuplicates(i)
        print(lc_singlelinkedlist2list(result))

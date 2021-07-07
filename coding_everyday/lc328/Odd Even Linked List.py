from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_head = odd = ListNode()
        even_head = even = ListNode()
        cnt = 1
        while head:
            if cnt % 2 != 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            cnt += 1

        if cnt % 2 != 0:
            odd.next = None
        else:
            even.next = None
        odd.next = even_head.next
        return odd_head.next


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [2, 1, 3, 5, 6, 4, 7],
    ]
    for i in test_cases:
        i = lc_list2singlelinkedlist(i)
        result = sol.oddEvenList(i)
        print(lc_singlelinkedlist2list(result))

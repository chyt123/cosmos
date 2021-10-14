from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        cnt = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            cnt += 1
        tail = None
        while slow:
            nxt = slow.next
            slow.next = tail
            tail = slow
            slow = nxt
        while head != tail and head.next != tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return head.val == tail.val


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 2, 3, 4],
        [1, 2, 2, 1],
        [1, 2, 3, 2, 1],
        [1, 2, 1],
        [1, 2],
    ]
    for i in test_cases:
        i = lc_list2singlelinkedlist(i)
        print(sol.isPalindrome(i))
        # print(lc_singlelinkedlist2list(result))

from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        if not head.next.next:
            if head.val > head.next.val:
                nxt = head.next
                head.next.next = head
                head.next = None
                return nxt
            return head
        rtn = ListNode()
        rtn.next = head
        slow = fast = rtn
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)
        rtn = tmp = ListNode()
        while left and right:
            if left.val <= right.val:
                tmp.next = left
                left = left.next
            else:
                tmp.next = right
                right = right.next
            tmp = tmp.next
        tmp.next = left if left else right
        return rtn.next


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [-1, 5, 3, 4, 0],
        [4, 2, 1, 3],
    ]
    for i in test_cases:
        i = lc_list2singlelinkedlist(i)
        result = sol.sortList(i)
        print(lc_singlelinkedlist2list(result))

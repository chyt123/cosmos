from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = set()
        while headA:
            a.add(headA)
            headA = headA.next
        while headB:
            if headB in a:
                return headB
            headB = headB.next
        return None


if __name__ == "__main__":
    sol = Solution()
    headA = [4, 1, 8, 4, 5]
    headB = [5, 6, 1, 8, 4, 5]
    headA = lc_list2singlelinkedlist(headA)
    headB = lc_list2singlelinkedlist(headB)
    tmpA = headA
    while tmpA.val != 8:
        tmpA = tmpA.next

    tmpB = headB
    while tmpB.val != 1:
        tmpB = tmpB.next
    tmpB.next = tmpA
    print(sol.getIntersectionNode(headA, headB))

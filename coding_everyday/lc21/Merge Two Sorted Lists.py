from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if not l1 or not l2:
        #     return l1 if l1 else l2
        dummy = ListNode(0)
        rtn = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        dummy.next = l1 if l1 else l2
        return rtn.next


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1, 2, 4], [1, 3, 4]],
        [[1, 2, 3, 4, 5], [1, 2, 3]],
        [[], []],
        [[], [0]],
    ]
    for i, j in test_cases:
        i = lc_list2singlelinkedlist(i)
        j = lc_list2singlelinkedlist(j)
        result = sol.mergeTwoLists(i, j)
        print(lc_singlelinkedlist2list(result))

import bisect
import collections
import copy
import math
from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        mod = k % n
        if mod == 0:
            return head
        pt = head
        for i in range(n - mod - 1):
            pt = pt.next
        rtn = pt.next
        pt.next = None
        tail.next = head
        return rtn


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1, 2, 3, 4, 5], 2],
        [[1, 2, 3, 4, 5, 6], 2],
        [[1, 2, 3, 4, 5, 6], 12],
        [[1, 2, 3], 4],
    ]
    for i, j in test_cases:
        result = (sol.rotateRight(lc_list2singlelinkedlist(i), j))
        print(lc_singlelinkedlist2list(result))

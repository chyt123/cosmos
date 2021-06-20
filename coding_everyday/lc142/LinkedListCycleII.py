from typing import List
from collections import defaultdict
from util import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        slow, fast = head, head
        while True:
            slow = slow.next
            fast = fast.next
            if not fast:
                return None
            fast = fast.next
            if not fast:
                return None
            if slow == fast:
                break
        fast = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


def lc_list2singlelinkedlistwithloop(l: List, pos: int) -> ListNode:
    ret = ListNode(l[0])
    cur = ret
    for i in range(0, len(l)):
        if i == 0:
            if i == pos:
                conn = cur
            continue
        cur.next = ListNode(l[i])
        cur = cur.next
        if i == pos:
            conn = cur
    cur.next = conn
    return ret


if __name__ == "__main__":
    sol = Solution()
    head = [3, 2, 0, -4]
    pos = 1
    head = [1,2]
    pos = 0
    head = lc_list2singlelinkedlistwithloop(head, pos)
    print(sol.detectCycle(head))

from typing import List
from util import ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        rtn = ListNode()
        rtn.next = head
        mem = [rtn]
        slow = fast = head
        scnt = fcnt = 0
        while fast and fast.next:
            mem.append(slow)
            slow = slow.next
            scnt += 1
            fast = fast.next.next
            fcnt += 2
        fcnt += 0 if not fast else 1
        idx = fcnt - n + 1
        while len(mem) < idx + 2 and slow:
            mem.append(slow)
            slow = slow.next
        if len(mem) < idx + 2:
            mem.append(None)
        mem[idx - 1].next = mem[idx + 1]
        return rtn.next


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[1, 2, 3, 4], 3],
        [[1, 2, 3, 4, 5], 2],
        [[1, 2, 3, 4, 5], 1]
    ]
    for i, j in test_cases:
        i = lc_list2singlelinkedlist(i)
        result = sol.removeNthFromEnd(i, j)
        print(lc_singlelinkedlist2list(result))

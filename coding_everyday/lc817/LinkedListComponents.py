from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        cnt = 0
        G = set(G)
        while G and head:
            if head.val in G:
                if not head.next or head.next.val not in G:
                    cnt += 1
                G.remove(head.val)
            head = head.next
        return cnt


if __name__ == "__main__":
    sol = Solution()
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
    G = [0, 1, 3]
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
    G = [0, 3, 1, 4]
    print(sol.numComponents(head, G))

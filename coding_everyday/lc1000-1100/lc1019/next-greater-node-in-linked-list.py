# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        l = [head.val]
        while head.next:
            head = head.next
            l.append(head.val)

        n = len(l)
        ans = [0] * n

        stack = [(l[0], 0)]
        for i in range(1, n):
            while stack and l[i] > stack[-1][0]:
                val, idx = stack.pop()
                ans[idx] = l[i]
            stack.append((l[i], i))

        return ans


# (5,0), (3,1), (1,2), 
# (5,0), (3,1), (2,3), 
# (5,0), (4,4)
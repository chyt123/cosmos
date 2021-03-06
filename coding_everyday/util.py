from typing import List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lc_tree2list(tree: TreeNode) -> List:
    q = deque([tree])
    ans = []
    while q:
        cur = q.popleft()
        if cur:
            ans.append(cur.val)
            q.extend([cur.left, cur.right])
        else:
            ans.append(None)
    idx = len(ans) - 1
    for i in range(idx, -1, -1):
        if ans[i] is not None:
            idx = i
            break
    return ans[:idx + 1]


def lc_list2tree(a: List) -> TreeNode:
    if not a:
        return None
    wait_list = []
    l = 0
    while a:
        lim = 2 ** l
        if lim == 1:
            cur = a.pop(0)
            ret = TreeNode(cur)
            wait_list.append(ret)
            l += 1
            continue
        for i in range(lim // 2):
            if not a:
                break
            left = a[0]
            right = None
            if len(a) > 1:
                right = a[1]

            if wait_list:
                cur_p = wait_list.pop(0)
                if cur_p:
                    cur_p.left = TreeNode(left) if left is not None else None
                    cur_p.right = TreeNode(right) if right is not None else None
                    a.pop(0)
                    if a:
                        a.pop(0)
                    wait_list.append(cur_p.left)
                    wait_list.append(cur_p.right)
        l += 1
    return ret


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def lc_list2singlelinkedlist(l: List) -> ListNode:
    if not l:
        return None
    ret = ListNode(l[0])
    cur = ret
    for i in range(1, len(l)):
        cur.next = ListNode(l[i])
        cur = cur.next
    return ret


def lc_singlelinkedlist2list(node: ListNode) -> List:
    ans = []
    while node:
        ans.append(node.val)
        node = node.next
    return ans
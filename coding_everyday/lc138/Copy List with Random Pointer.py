import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        mem_new = dict()
        mem_old = dict()
        hd = head
        rtn = cur = Node(head.val)
        idx = 0
        while head.next:
            mem_new[idx] = cur
            mem_old[head] = idx
            cur.next = Node(head.next.val)
            head = head.next
            cur = cur.next
            idx += 1
        mem_new[idx] = cur
        mem_old[head] = idx
        cur = rtn
        while hd:
            cur.random = mem_new[mem_old[hd.random]] if hd.random else None
            hd = hd.next
            cur = cur.next
        return rtn


if __name__ == "__main__":
    sol = Solution()
    # test_cases = [
    #     [2,2,3,2],
    #     [0,1,0,1,0,1,99]
    # ]
    # for i in test_cases:
    #     print(sol.singleNumber(i))

import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


# O(1) time and use O(h) memory
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.q = []
        self.idx = 0
        self.inorder_trav(root)

    def inorder_trav(self, root):
        if root:
            self.inorder_trav(root.left)
            self.q.append(root.val)
            self.inorder_trav(root.right)

    def next(self) -> int:
        rtn = self.q[self.idx]
        self.idx += 1
        return rtn

    def hasNext(self) -> bool:
        return self.idx < len(self.q)


if __name__ == "__main__":
    cmd = ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    val = [[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]
    for idx, i in enumerate(cmd):
        if i == "BSTIterator":
            bst = BSTIterator(lc_list2tree(val[0][0]))
        elif i == "next":
            print(bst.next())
        elif i == "hasNext":
            print(bst.hasNext())

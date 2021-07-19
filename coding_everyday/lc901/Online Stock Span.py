import collections
import math
from typing import List
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class StockSpanner:

    def __init__(self):
        self.prices = []
        self.span = []

    def find_span(self, cur):
        if cur == 0:
            return 1
        pre = cur - 1
        cnt = 1
        while pre >= 0 and self.prices[pre] <= self.prices[cur]:
            cnt += self.span[pre]
            pre = pre - self.span[pre]
        return cnt

    def next(self, price: int) -> int:
        self.prices.append(price)
        self.span.append(self.find_span(len(self.prices) - 1))
        return self.span[-1]


if __name__ == "__main__":
    rle = StockSpanner()

    cmds = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    vals = [[], [80], [100], [60], [70], [60], [75], [85]]
    for i in range(len(cmds)):
        if cmds[i] == 'next':
            print(rle.next(vals[i][0]))
import bisect
import collections
import copy
import functools
import math
from typing import List, Optional
from collections import defaultdict
from util import TreeNode, lc_tree2list, lc_list2tree, ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.strip('-').isnumeric():
                stack.append(i)
            else:
                r = stack.pop()
                l = stack.pop()
                stack.append(str(int(eval(l + i + r))))
        return int(stack[0])


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["2","1","+","3","*"],
        ["4","13","5","/","+"],
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
    ]
    for i in test_cases:
        result = sol.evalRPN(i)
        print(result)

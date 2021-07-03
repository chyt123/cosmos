import bisect
import math
import heapq
from typing import List
from collections import deque, defaultdict


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        cur = self.stack.pop()
        if cur == self.min_stack[-1]:
            self.min_stack.pop()
        return cur

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == "__main__":
    min_stack = MinStack()
    op = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    val = [[], [-2], [0], [-3], [], [], [], []]
    for i in range(1, len(op)):
        if op[i] == 'push':
            min_stack.push(val[i][0])
        elif op[i] == 'getMin':
            print(min_stack.getMin())
        elif op[i] == 'pop':
            print(min_stack.pop())
        elif op[i] == 'top':
            print(min_stack.top())

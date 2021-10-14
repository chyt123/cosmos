import bisect
import collections
from typing import List


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        while self.q[0] != x:
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


if __name__ == "__main__":
    stack = MyStack()
    ops = ["push", "push", "top", "pop", "empty"]
    vals = [[1], [2], [], [], []]
    for idx, i in enumerate(ops):
        if i == 'push':
            stack.push(vals[idx][0])
        elif i == 'top':
            print(stack.top())
        elif i == 'pop':
            print(stack.pop())
        elif i == 'empty':
            print(stack.empty())


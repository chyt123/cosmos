# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.tree = root if root else TreeNode(0) # 3 - 01 4-000 5-001 6-010 7-011 8-0000 9-0001
        self.l = []
        self.trans(self.tree)

        print(self.l)
        self.cnt = len(self.l)

    def trans(self, node):
        if node:
            self.trans(node.left)
            self.trans(node.right)
            self.l.append(node.val)

    def insert(self, val: int) -> int:
        self.cnt += 1
        level = math.floor(math.log2(self.cnt))

        code_num = self.cnt - 2**level
        code = format(code_num, 'b').zfill(level)
        # print(code)

        node = self.tree
        for i in range(0, len(code) - 1):
            # 0 left, 1 right
            if code[i] == '0':
                node = node.left
            else:
                node = node.right

        ans = node.val
        if code[-1] == '0':
            node.left = TreeNode(val)
        else:
            node.right = TreeNode(val)
        # print(self.tree)

        return ans

    def get_root(self) -> Optional[TreeNode]:
        return self.tree



# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
import bisect
import collections
from typing import List


class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None


class NumArray:

    def __init__(self, nums: List[int]):
        def create_tree(start, end):
            node = Node(start, end)
            node.total = sum(nums[start:end + 1])
            mid = (start + end) // 2
            if start != end:
                node.left = create_tree(start, mid)
                node.right = create_tree(mid + 1, end)
            return node

        self.root = create_tree(0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        def update_val(root):
            if not root or not root.start <= index <= root.end:
                return 0
            if root.start == root.end == index:
                diff = root.total - val
                root.total = val
                return diff
            diff = update_val(root.left) + update_val(root.right)
            root.total -= diff
            return diff

        update_val(self.root)

    def sumRange(self, left: int, right: int) -> int:
        def find_sum(root, l, r):
            if l == root.start and r == root.end:
                return root.total
            mid = (root.start + root.end) // 2
            if r <= mid:
                return find_sum(root.left, l, r)
            elif l >= mid + 1:
                return find_sum(root.right, l, r)
            else:
                return find_sum(root.left, l, mid) + find_sum(root.right, mid + 1, r)

        return find_sum(self.root, left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)


if __name__ == "__main__":
    ops = ["NumArray", "sumRange", "update", "sumRange"]
    vals = [[1, 3, 5], [0, 2], [1, 2], [1, 2]]
    ops = ["NumArray", "sumRange", "sumRange", "sumRange", "update", "update", "update", "sumRange", "update", "sumRange",
     "update"]
    vals = [[0, 9, 5, 7, 3], [4, 4], [2, 4], [3, 3], [4, 5], [1, 7], [0, 8], [1, 2], [1, 9], [4, 4], [3, 4]]
    num_array = NumArray(vals[0])
    for idx, i in enumerate(ops):
        if i == 'sumRange':
            print(num_array.sumRange(vals[idx][0], vals[idx][1]))
        elif i == 'update':
            num_array.update(vals[idx][0], vals[idx][1])
    print('hello')

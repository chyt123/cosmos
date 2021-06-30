from typing import List
from collections import deque, OrderedDict
import heapq


class Leaf:
    def __init__(self, content: str):
        self.content = content

    @property
    def length(self):
        return len(self.content)


class Internal:
    def __init__(self):
        self.left = None
        self.right = None

    @property
    def length(self):
        ans = 0
        if self.left:
            ans += self.left.length
        if self.right:
            ans += self.right.length
        return ans


def nth_character(root, n) -> str:
    """
    Return nth character in the cord, 0 based
    if invalid, return ''
    """
    # Edge cases
    if not root:
        return ''
    cur_n = root.length
    if n < 0 or n >= cur_n:
        return ''

    # if root is Leaf
    if isinstance(root, Leaf):
        return root.content[n]

    # else root is Internal
    left_len = root.left.length
    if n < left_len:  # at left
        return nth_character(root.left, n)
    else:  # at right
        return nth_character(root.right, n - left_len)


def find_string(root, n, l):
    if not root:
        return ''
    cur_n = root.length
    if n < 0 or n >= cur_n:
        return ''

    if n + l > root.length:
        remain = n + l - root.length
        l = root.length - n
    else:
        remain = 0

    # if root is Leaf
    if isinstance(root, Leaf):
        ans = root.content[n:n + l]
        return ans, remain

    ans = ''
    # else root is Internal
    left_len = root.left.length
    if n < left_len:  # start at left
        ans, remain = find_string(root.left, n, l)
        new_n = 0
    else:
        new_n = n - left_len
        remain = l
    right_ans, remain = find_string(root.right, new_n, remain)
    ans += right_ans
    return ans, remain


def delete_string(root, n, l):
    if not root:
        return ''
    cur_n = root.length
    if n < 0 or n >= cur_n:
        return ''

    if n + l > root.length:
        remain = n + l - root.length
        l = root.length - n
    else:
        remain = 0

    # if root is Leaf
    if isinstance(root, Leaf):
        root.content = root.content[:n] + root.content[n + l:]
        return remain

    # else root is Internal
    left_len = root.left.length
    if n < left_len:  # start at left
        remain = delete_string(root.left, n, l)
        new_n = 0
    else:
        new_n = n - left_len
        remain = l
    remain = delete_string(root.right, new_n, remain)
    if isinstance(root.left, Internal):
        old_left = root.left
        if not old_left.left.length:
            root.left = root.left.right
        if not old_left.right.length:
            root.left = root.left.left
    if isinstance(root.right, Internal):
        old_right = root.right
        if not old_right.left.length:
            root.right = root.right.right
        if not old_right.right.length:
            root.right = root.right.left
    return remain


class Solution:
    pass


if __name__ == "__main__":
    # sol = Solution()
    # print(sol.print_structure(paths))
    ae = Leaf('ABCDE')
    fo = Leaf('FGHIJKLMNO')
    pz = Leaf('PQRSTUVWXYZ')
    root = Internal()
    right_root = Internal()
    # root.length = 26
    root.left = ae
    root.right = right_root
    # right_root.length = 21
    right_root.left = fo
    right_root.right = pz
    for i in range(26):
        print(nth_character(root, i))
    n = 4
    l = 15
    print(find_string(root, n, l))
    delete_string(root, n, l)
    print(root)
    print()

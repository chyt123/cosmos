import collections
from typing import List, Optional
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        q = collections.deque([root])
        while q:
            l = len(q)
            for _ in range(l):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    if cur.val == targetSum:
                        return True
                if cur.left:
                    cur.left.val += cur.val
                    q.append(cur.left)
                if cur.right:
                    cur.right.val += cur.val
                    q.append(cur.right)
        return False


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22],
        [[1,2,3], 5],
        [[1,2], 0],
    ]
    for i, j in test_cases:
        result = sol.hasPathSum(lc_list2tree(i), j)
        print(result)


import collections
from typing import List, Optional
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = collections.deque([root])
        lv = 1
        end_flag = False
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if not cur.left and not cur.right:
                    end_flag = True
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if end_flag:
                break
            lv += 1
        return lv


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 9, 20, None, None, 15, 7],
        [2, None, 3, None, 4, None, 5, None, 6],
    ]
    for i in test_cases:
        result = sol.minDepth(lc_list2tree(i))
        print(result)


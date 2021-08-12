from typing import List, Optional
from collections import deque
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        reverse = False
        while q:
            l = len(q)
            ans.append([])
            for _ in range(l):
                cur = q.popleft()
                ans[-1].append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if reverse:
                ans[-1].reverse()
            reverse = not reverse
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [3, 9, 20, None, None, 15, 7],
        [1],
        []
    ]
    for i in test_cases:
        print(sol.zigzagLevelOrder(lc_list2tree(i)))

import collections
from typing import List, Optional
from util import (
    ListNode, lc_list2singlelinkedlist, lc_singlelinkedlist2list,
    TreeNode, lc_tree2list, lc_list2tree
)


class TreeNodeWithParent(TreeNode):
    def __init__(self, val=0, left=None, right=None, parent=None):
        super(TreeNodeWithParent, self).__init__(val, left, right)
        self.parent = parent

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        def dfs(node, new_node):
            cur_node = TreeNodeWithParent(node.val + new_node.val) if new_node else TreeNodeWithParent(node.val)
            cur_node.parent = new_node
            if not node.left and not node.right and cur_node.val == targetSum:
                prepare_ans(cur_node)
            if node.left:
                cur_node.left = dfs(node.left, cur_node)
            if node.right:
                cur_node.right = dfs(node.right, cur_node)
            return cur_node

        def prepare_ans(node):
            tmp = []
            while node:
                if node.parent:
                    tmp.append(node.val - node.parent.val)
                else:
                    tmp.append(node.val)
                node = node.parent
            tmp.reverse()
            ans.append(tmp)
        dfs(root, None)
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [[5,4,8,11,None,13,4,7,2,None,None,5,1], 22],
        [[1,2,3], 5],
    ]
    for i, j in test_cases:
        result = sol.pathSum(lc_list2tree(i), j)
        print(result)


from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = root

        def mot(root_node: 'TreeNode', p, q):
            l, r, m = 0, 0, 0
            if root_node.val in [p.val, q.val]:
                m = 1
            if root_node.left:
                l = mot(root_node.left, p, q)
            if root_node.right:
                r = mot(root_node.right, p, q)
            if l + r + m >= 2:
                self.ans = root_node
            return 1 if l + r + m > 0 else 0

        mot(root, p, q)
        return self.ans


        # Too Slow
        # p_parent, q_parent = [p.val], [q.val]
        #
        # def find_parent(root_node: 'TreeNode', p_list):
        #     if root_node.left:
        #         find_parent(root_node.left, p_list)
        #     if root_node.right:
        #         find_parent(root_node.right, p_list)
        #
        #     if root_node.left and root_node.left.val == p_list[-1]:
        #         p_list.append(root_node.val)
        #     if root_node.right and root_node.right.val == p_list[-1]:
        #         p_list.append(root_node.val)
        #
        # find_parent(root, p_parent)
        # find_parent(root, q_parent)
        #
        # while p_parent and q_parent and p_parent[-1] == q_parent[-1]:
        #     ans = p_parent.pop()
        #     q_parent.pop()
        #
        # return TreeNode(ans)


if __name__ == "__main__":
    sol = Solution()
    # root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
    tn = [TreeNode(0)] * 9
    for i in range(9):
        tn[i] = TreeNode(i)

    tn[3].left = tn[5]
    tn[3].right = tn[1]
    tn[5].left = tn[6]
    tn[5].right = tn[2]
    tn[1].left = tn[0]
    tn[1].right = tn[8]
    tn[2].left = tn[7]
    tn[2].right = tn[4]

    print(sol.lowestCommonAncestor(tn[3], tn[5], tn[4]))

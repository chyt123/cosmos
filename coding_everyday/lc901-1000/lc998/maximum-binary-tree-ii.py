# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # node_list = []

        # def mid_trav(node):
        #     if not node:
        #         return
        #     mid_trav(node.left)
        #     node_list.append(node.val)
        #     mid_trav(node.right)

        # mid_trav(root)

        # node_list.append(val)

        # # Construct
        # def construct(l):
        #     if not l:
        #         return None
        #     idx = l.index(max(l))
        #     node = TreeNode(l[idx])
        #     node.left = construct(l[:idx])
        #     node.right = construct(l[idx + 1:])
        #     return node

        # return construct(node_list)

        new_node = TreeNode(val)
        if root.val < val:
            new_node.left = root
            return new_node

        node = root
        while node and node.val > val:
            pre_node = node
            node = node.right

        new_node.left = node
        pre_node.right = new_node

        return root
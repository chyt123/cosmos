from typing import List
from collections import deque, defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def add_graph(node):
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                add_graph(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                add_graph(node.right)

        add_graph(root)

        visit = [False] * len(graph)
        lv = []
        stack = deque([target.val, '@'])
        e = []
        while stack:
            cur = stack.popleft()
            if cur == '@':
                lv.append(e)
                e = []
                if not stack:
                    break
                stack.append('@')
            elif cur < len(visit) and not visit[cur]:
                visit[cur] = True
                for i in graph[cur]:
                    stack.append(i)
                e.append(cur)
        if k < len(lv):
            return lv[k]
        return []


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
    print(sol.distanceK(tn[3], tn[5], 2))

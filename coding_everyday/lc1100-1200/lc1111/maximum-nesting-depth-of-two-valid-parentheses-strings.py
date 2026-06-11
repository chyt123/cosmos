class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        n = len(seq)
        ans = [0] * n
        stack = []

        deepest = 0
        for i in range(n):
            if seq[i] == '(':
                stack.append(seq[i])
                ans[i] = len(stack)
            else:
                ans[i] = len(stack)
                stack.pop()
            deepest = max(deepest, ans[i])

        # print(ans, deepest)
        for i in range(n):
            ans[i] = 0 if ans[i] <= deepest // 2 else 1

        return ans

# 1 -> nothing, 2-> 1 2, 3 -> 1/2 3, 4-> 12/34

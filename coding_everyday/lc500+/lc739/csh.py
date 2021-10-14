class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # Output limit exceeded ?????
        lt = len(T)
        rst = [0] * lt
        s = 0

        for i in xrange(lt - 1, -1, -1):
            if T[i] > T[i - 1]:
                rst[i - 1] = 1
            if rst[i] != 1:
                rst[i] = s
            else:
                if i < lt - 1 and rst[i + 1] != 1:
                    s = 0
            s += rst[i]
        return rst

        # AC
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)

        return ans


if __name__ == "__main__":
    sol = Solution()
    T = [71, 71, 71, 71, 71, 71, 71, 71, 71, 71]
    T = [76, 75, 73, 74, 75, 71, 69, 72, 76, 73]
    print sol.dailyTemperatures(T)

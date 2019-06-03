class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        strl = [int(d) for d in str(N)]
        return_flag = True
        for i in range(len(strl) - 1, 0, -1):
            cur = strl[i]
            pre = strl[i - 1]
            if cur < pre:
                return_flag = False
                strl[i - 1] = pre - 1
                for j in range(i, len(strl)):
                    strl[j] = 9

        if return_flag:
            return N
        else:
            return self.monotoneIncreasingDigits(int(''.join(map(str, strl))))


if __name__ == "__main__":
    sol = Solution()
    N = 1235
    print sol.monotoneIncreasingDigits(N)

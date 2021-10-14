class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        for i in range(N):
            strn = str(i)
            if '3' in strn or '4' in strn or '7' in strn:
                continue
            if '2' in strn or '5' in strn or '6' in strn or '9' in strn:
                cnt += 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    N = 857
    print sol.rotatedDigits(N)


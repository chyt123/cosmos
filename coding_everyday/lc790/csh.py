from collections import Counter


class Solution(object):
    def numTilings(self, N):
        if N <= 1:
            return 1
        rst = [1] * (N + 1)
        rst[2] = 2
        for i in range(3,len(rst)):
            rst[i] = 2 * rst[i - 1] + rst[i - 3]

        return rst[-1] % (pow(10, 9) + 7)


if __name__ == "__main__":
    sol = Solution()
    N = 3
    print sol.numTilings(N)


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        d = [0]
        rst = 0
        lflag = -1
        rflag = -1
        for i, num in enumerate(A):
            if L <= num <= R:
                d.append(d[i] + i - lflag)
                rflag = i
            elif num < L:
                d.append(d[i] + max(0, rflag - lflag))
            elif num > R:
                d.append(0)
                lflag = i
                rst += d[i]
        rst += d[-1]
        return rst


if __name__ == "__main__":
    sol = Solution()
    A = [2, 1, 4, 3]
    L = 2
    R = 3
    print sol.numSubarrayBoundedMax(A, L, R)


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        d = [0]
        rst = 0
        flag = -1
        for i, num in enumerate(A):
            if L <= num and i <= num:
                d.append(d[i] + i - flag)
                rst = d[-1]
            elif num < L:
                d.append(d[i] + i)
                rst = d[-1]
            elif num > R:
                d.append(0)
                flag = i
            print d
        return rst

if __name__ == "__main__":
    sol = Solution()
    A = [2, 1, 4, 3]
    L = 2
    R = 3
    print sol.numSubarrayBoundedMax(A, L, R)


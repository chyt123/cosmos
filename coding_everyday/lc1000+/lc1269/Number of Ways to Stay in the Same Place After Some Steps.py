MOD = 1000000007
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        boundary = min(arrLen, steps + 1)
        arr = [[0 for _ in range(boundary)] for _ in range(steps + 1)]
        arr[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(boundary):
                if j - 1 >= 0:
                    arr[i][j] += arr[i - 1][j - 1]
                if j + 1 < boundary:
                    arr[i][j] += arr[i - 1][j + 1]
                arr[i][j] += arr[i - 1][j]
        return arr[-1][0] % MOD


# [1,0,0,0,0] 6:3 5:2 4:2
# [1,1,0,0,0]
# [2,2,1,0,0]
# [0,0,0,0,0]
# [0,0,0,0,0]
# [0,0,0,0,0]
# [0,0,0,0,0]
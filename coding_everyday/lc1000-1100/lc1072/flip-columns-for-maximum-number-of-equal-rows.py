class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # def flip_same(a, b):
        #     if a == b:
        #         return True
        #     b = ''.join('1' if x == '0' else '0' for x in b)
        #     return a == b

        binstr = []
        for i in matrix:
            i = map(str, i)
            binstr.append(''.join(i))
        
        # dp = [1] * m
        # ans = 0
        # for i in range(1, m):
        #     for j in range(i - 1, -1, -1):
        #         if flip_same(binstr[i], binstr[j]):
        #             dp[i] = max(dp[i], dp[j] + 1)
        #     ans = max(ans, dp[i])
        
        # return ans

        s = defaultdict(int)
        for i in binstr:
            s[i] += 1
            i = ''.join('1' if x == '0' else '0' for x in i)
            s[i] += 1
        
        summary = []
        for i in s:
            summary.append((i, s[i]))
        summary = sorted(summary, key=lambda x: -x[1])

        return summary[0][1]



# 0 1
# 1 0

# 0 0 0 1
# 0 0 1 1
# 1 1 0 0
# 0 0 1 0

# count max num of same rows (fliped or not)

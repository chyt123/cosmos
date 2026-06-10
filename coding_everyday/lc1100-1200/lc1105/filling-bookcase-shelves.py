class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)

        dp[0] = 0
        dp[1] = books[0][1]

        for i in range(1, n):
            cur_w = books[i][0]
            cur_h = books[i][1]
            dp[i + 1] = dp[i] + cur_h
            for j in range(i - 1, -1, -1):
                wj = books[j][0]
                hj = books[j][1]
                if cur_w + wj <= shelfWidth:
                    cur_h = max(cur_h, hj)
                    dp[i + 1] = min(dp[i + 1], dp[j] + cur_h)
                    cur_w += wj
                else:
                    break

        # print(dp)
        return dp[-1]

# w = 3
# 1 2 3 4 5
# 5 4 3 2 1

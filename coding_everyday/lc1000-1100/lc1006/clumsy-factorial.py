class Solution:
    def clumsy(self, n: int) -> int:
        ans =  n * (n - 1) // (n - 2) if n > 2 else n
        for i in range(n - 4, 0, -4):
            if i in [1, 2]:
                ans -= i
            else:
                ans -= i * (i - 1) // (i - 2)

        for i in range(n - 3, 0, -4):
            ans += i

        return ans

# test cases
# 3 => 3 * 2 // 1
# 4 => 4 * 3 // 2, + 1
# 5 => 5 * 4 // 3, - 1, + 2
# 8 => 8 * 7 // 6, - 4 * 3 // 2 + 5 + 1
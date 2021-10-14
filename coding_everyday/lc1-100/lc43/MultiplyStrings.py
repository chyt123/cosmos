from typing import List


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def myint(ch):
            return ord(ch) - ord('0')

        ans = 0
        for i in range(len(num2) - 1, -1, -1):
            a = ''
            plus = 0
            m = myint(num2[i])
            for j in range(len(num1) - 1, -1, -1):
                n = myint(num1[j])
                cal = m * n + plus
                a = str(cal % 10) + a
                plus = cal // 10
            if plus:
                a = str(plus) + a
            ans += int(a) * 10 ** (len(num2) - i - 1)

        return str(ans)


if __name__ == "__main__":
    sol = Solution()
    num1 = "9"
    num2 = "9"
    print(sol.multiply(num1, num2))

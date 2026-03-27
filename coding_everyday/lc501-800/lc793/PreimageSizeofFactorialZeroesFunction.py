from math import log


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        a = [1]
        for i in range(13):
            a.append(a[-1] * 5 + 1)
        a.reverse()
        for i in a:
            if k / i == 5:
                return 0
            k %= i
        return 5


if __name__ == "__main__":
    sol = Solution()
    k = 1
    print(sol.preimageSizeFZF(k))

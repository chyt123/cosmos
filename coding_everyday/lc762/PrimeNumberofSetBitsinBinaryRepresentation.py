import math


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        def is_prime(n):
            if n == 2:
                return True
            if n < 2 or n % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return False
            return True

        cnt = 0
        for i in range(L, R + 1):
            n = '{0:b}'.format(i).count('1')
            if is_prime(n):
                cnt += 1

        return cnt


if __name__ == "__main__":
    sol = Solution()
    L = 6
    R = 10
    L = 10
    R = 15
    print(sol.countPrimeSetBits(L, R))

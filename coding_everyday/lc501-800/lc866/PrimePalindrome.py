import math
from typing import List
from collections import deque, defaultdict

class Solution:
    def primePalindrome(self, n: int) -> int:
        def is_prime(num):
            if num < 2:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, math.floor(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
            return True

        e = math.floor(math.log10(n))
        for l in range(e, 9):
            check = l // 2
            for i in range(10 ** check, 10 ** (check + 1)):
                num = int(str(i) + str(i)[::-1]) if l % 2 != 0 else int(str(i) + str(i)[-2::-1])
                if num >= n and is_prime(num):
                    return num


if __name__ == "__main__":
    sol = Solution()
    n = 2
    print(sol.primePalindrome(n))

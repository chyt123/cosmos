from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for i in range(left, right+1):
            ret = self.is_self_divide(i)
            if ret:
                ans.append(i)
        return ans

    def is_self_divide(self, n):
        sn = str(n)
        for s in sn:
            if s == '0' or n % int(s) != 0:
                return None
        return n


if __name__ == "__main__":
    sol = Solution()
    left = 1
    right = 22
    print(sol.selfDividingNumbers(left, right))

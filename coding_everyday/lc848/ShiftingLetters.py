from typing import List


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        num = 0
        ans = ''
        for i in range(len(S) - 1, -1, -1):
            num += shifts[i] % 26
            new_asc = (ord(S[i]) + num - 19) % 26 + 97
            ans = chr(new_asc) + ans
        return ans


if __name__ == "__main__":
    sol = Solution()
    S = "abc"
    shifts = [3, 5, 9]
    print(sol.shiftingLetters(S, shifts))

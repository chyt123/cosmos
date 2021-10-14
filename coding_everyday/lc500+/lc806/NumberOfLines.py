from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        cur = 0
        for ch in s:
            idx = ord(ch) - 97
            cur += widths[idx]
            if cur > 100:
                line += 1
                cur = widths[idx]

        return [line, cur]


if __name__ == "__main__":
    sol = Solution()
    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "abcdefghijklmnopqrstuvwxyz"
    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "bbbcccdddaaa"
    print(sol.numberOfLines(widths, s))


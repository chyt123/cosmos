import bisect
import collections
from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        cur = ''
        post_symbol = ''
        post = ''

        for i in s:
            if i == ' ':
                continue
            if i.isnumeric():
                if not post_symbol:
                    cur += i
                else:
                    post += i
            else:
                if post_symbol:
                    cur = str(int(cur) * int(post)) if post_symbol == '*' else str(int(int(cur) / int(post)))
                if i in ['+', '-']:
                    result += int(cur)
                    cur = i
                    post_symbol = ''
                elif i in ['*', '/']:
                    post_symbol = i
                    post = ''

        if post_symbol:
            cur = str(int(cur) * int(post)) if post_symbol == '*' else str(int(int(cur) / int(post)))
        result += int(cur)

        return result


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "3+2*2",
        " 3/2 ",
        " 3+5 / 2 ",
        " 3+5 / 2 * 3 - 4 *2",
        "14-3/2"
    ]
    for i in test_cases:
        print(sol.calculate(i))


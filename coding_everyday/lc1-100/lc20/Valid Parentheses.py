from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                cur = stack.pop()
                if ch == ')' and cur != '(' or \
                    ch == ']' and cur != '[' or \
                    ch == '}' and cur != '{':
                    return False
        return not stack


if __name__ == "__main__":
    sol = Solution()
    s = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
    ]
    for i in s:
        print(sol.isValid(i))

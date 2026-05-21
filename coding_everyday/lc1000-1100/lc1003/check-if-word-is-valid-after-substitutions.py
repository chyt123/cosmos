class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] != 'a' or s[-1] != 'c':
            return False

        n = len(s)
        stack = []
        for c in s:
            stack.append(c)
            if c == 'c':
                if len(stack) >= 3 and ''.join(stack[-3:]) == 'abc':
                    for i in range(3):
                        stack.pop()
                else:
                    return False

        return True if not stack else False

                

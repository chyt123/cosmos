class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.type_str(s) == self.type_str(t)

    @staticmethod
    def type_str(ms):
        rst = []
        for i in ms:
            if i != '#':
                rst.append(i)
            elif rst:
                rst.pop()
        return rst


if __name__ == "__main__":
    sol = Solution()
    s = "ab#c"
    t = "ad#c"
    s = "ab##"
    t = "c#d#"
    s = "a##c"
    t = "#a#c"
    s = "a#c"
    t = "b"
    print(sol.backspaceCompare(s, t))

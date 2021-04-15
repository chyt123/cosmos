from typing import List
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        rst = []
        l = len(s)
        i = 0
        while i < l-2:
            cnt = 1
            for j in range(i+1, l):
                if s[j] == s[i]:
                    cnt += 1
                if s[j] != s[i] or j == l-1:
                    if cnt >= 3:
                        rst.append([i, i+cnt-1])
                    i += cnt
                    break
        return rst


if __name__ == "__main__":
    sol = Solution()
    s = "aaa"
    print(sol.largeGroupPositions(s))

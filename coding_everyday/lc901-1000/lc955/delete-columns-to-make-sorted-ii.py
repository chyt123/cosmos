from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        ans = 0

        i = 1
        while 1 <= i < n:
            stop = False
            while strs[i] < strs[i - 1]:
                if stop:
                    break
                for j in range(len(strs[0])):
                    if ord(strs[i][j]) < ord(strs[i - 1][j]):
                        # print(i, strs[i], strs[i - 1])
                        # print(strs)
                        ans += 1
                        for k in range(n):
                            strs[k] = strs[k][:j] + strs[k][j + 1:]
                            stop = True
                        break
            if not stop:
                i += 1
            else:
                i = 1
        return ans

# aba
# bab
# aba
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ["zyx","wvu","tsr"],
        ["aba","bab","aba"]
    ]
    for i in test_cases:
        print(sol.minDeletionSize(i))